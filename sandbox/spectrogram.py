import os
import numpy as np
from scipy.io import wavfile
from scipy import signal
import matplotlib.pyplot as plt

HOME = os.path.expanduser('~')

### Read a wavfile
(fs, x) = wavfile.read(HOME+"/wav/embraceableYou.wav")
if x.ndim > 1: x = x[:,1]

N = x.shape[0]

### Write a wavfile
#wavfile.write('bla.wav', fs, y)

### Get the duration of the file
seconds_duration_of_file = N / float(fs) 

### Get the 
x.shape # 2 columns because stereo (L, R)

#### Get the time index (also sampled every 500)
t = (np.arange(0, N) / float(fs)) / 60 # minutes


### Plot the wave

plt.plot(t, x) # get every 500
plt.show()

### Plot FFT
#plt.plot(t, np.abs(np.fft.fft(xs)))
#plt.show()

### Blackman Window.

### Plot Spectrogram
window = signal.blackman(4096)
f, t, Sxx = signal.spectrogram(x, fs, window=window)

THRESH_MAX = 50000
THRESH_MIN = 30000

#trans = np.vectorize(lambda s: THRESH_MAX if s > THRESH_MAX else s)
#trans = np.vectorize(lambda s: s)
trans = np.vectorize(lambda s: 1 if s > THRESH_MIN else 0)
tS = trans(Sxx)
plt.pcolormesh(t, f, tS)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.ylim([0, 4400])
plt.show()

Sxx.shape

### ID Predominant Pitches
from notes import pitch
pitch = np.vectorize(pitch)
M = np.argwhere(tS == 1)
pitches = pitch(f[M[:,0]])
seconds = t[M[:,1]]

order = np.argsort(seconds)
pitches[order]
seconds[order]

from itertools import groupby
from operator import itemgetter

W = zip(*(seconds[order], pitches[order]))

d = {}
for w in W:
    w0 = float(w[0])
    w1 = w[1]
    if d.has_key(w0): d[w0].add(w1)
    else: d[w0] = set([w1])


l = map(lambda k: (k,d[k]), sorted(d.keys()))
s = filter(lambda x: 164.5 < x < 165.5, d.keys())
map(lambda k: d[k], s)
