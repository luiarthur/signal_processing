import numpy as np
import pandas as pd
from scipy import signal

A4 = 440.0
C0 = A4*pow(2, -4.75)
#name = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
name = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    
def pitch_unvec(freq):
    h = 12 * np.log(freq/A4) / np.log(2)
    n = int(round(h % 12))
    n = n if n < 12 else 0
    octave = int(round(h) // 12 + 4)
    if n > 2:
        octave += 1
    return name[n] + str(octave)

pitch = np.vectorize(pitch_unvec)

piano_freq = []
with open("piano_freq.txt") as f:
    for line in f.readlines():
        piano_freq += [ float(line) ]
    f.close()

piano_freq.reverse()
#print pitch(piano_freq)
assert len(set(pitch(piano_freq))) == len(pitch(piano_freq)) == 88

freq_dict = dict()
piano_pitches = pitch(piano_freq)
for i in range(88):
    freq_dict[piano_pitches[i]] = piano_freq[i]

#pitch(559)

### All the pitches on piano
#from collections import OrderedDict
#p_set = pitch(np.arange(28,4188))

def closest_piano_freq(f):
    return np.array(map(lambda x: freq_dict[x], pitch(f)))

def bin_spec(f, t, S, min_freq=27, max_freq=4200, S_max=None):
    #idx = np.argwhere(min_freq <= f and f <= max_freq)
    idx = np.argwhere((min_freq <= f) * (f <= max_freq)).T[0]
    f = f[idx]
    Z = S[idx,:]

    # Get pitches corresponding to freqs
    index = pd.Index(closest_piano_freq(f), name='pf')
    df = pd.DataFrame(Z, index=index)
    Z_new = df.groupby('pf').max()
    #df.groupby(['pitch']).mean().as_matrix()
    #df.groupby(['pitch']).max().as_matrix()
    f_new = Z_new.index.values
    Z_new = Z_new.as_matrix()
    #Z_new = Z
    #f_new = f

    #mx = Z_new.max() if S_max is None else S_max
    #return f_new, t, np.exp( np.log(Z_new) - np.log(mx) )

    # version2:
    mm = np.kron(np.ones(Z_new.shape[0]), np.asmatrix(np.max(Z,0)).T)
    #print mm
    #print np.max(Z,0)
    return f_new, t, np.asarray(np.exp( np.log(Z_new) - np.log(mm.T) ))


def my_spectrogram(x, fs, nperseg=2**14, window=None, noverlap=8):
    if window is None:
        window = signal.get_window('blackman', Nx=nperseg)

    f, t, Zxx = signal.spectrogram(x, fs, nperseg=nperseg, window=window, noverlap=noverlap)
    return bin_spec(f, t, Zxx)

