import os
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

HOME = os.path.expanduser('~')

### Read a wavfile
(fs, x) = wavfile.read(HOME+"/wav/embraceableYou.wav")

### Write a wavfile
#wavfile.write('bla.wav', fs, y)

### Get the duration of the file
seconds_duration_of_file = x.shape[0] / float(fs) 

### Get the 
x.shape # 2 columns because stereo (L, R)

### Sampled Wave (every 500)
every = 500
xs = x[::every,0]

### Get the time index (also sampled every 500)
t = (np.arange(0,x.shape[0],every) / float(fs)) / 60 # minutes


### Plot the wave
#plt.plot(t, xs) # get every 500
#plt.show()

### Plot FFT
#plt.plot(t, np.abs(np.fft.fft(xs)))
#plt.show()

### Blackman Window.
from scipy import signal
#window = signal.blackman(50)
#plt.figure()
#A = np.fft.fft(window, 4096) / (len(window) / 2.0)
#f = np.linspace(-.5, .5, len(A))
#response = 20 * np.log10(np.abs(np.fft.fftshift(A / abs(A).max())) + 1E-6)
##response = 20 * np.log10(np.abs(np.fft.fftshift(A)) / np.abs(abs(A)).max() + 1E-6)
#plt.plot(f, response)
#plt.show()

### Plot Spectrogram
#xm = x[:,0]
xm = np.mean(x, 1)
N = xm.size
window = signal.blackman(4096)
f, t, Sxx = signal.spectrogram(xm, fs, window=window)

### Truncate at max frequency
F_MAX = 4400
f_imax = np.argmin(f <= F_MAX)
f = f[:f_imax]
Sxx = Sxx[:f_imax,:]
#plt.pcolormesh(t, f, np.power(Sxx, .25))

THRESH_MAX = 50000
THRESH_MIN = 30000

#trans = np.vectorize(lambda s: THRESH_MAX if s > THRESH_MAX else s)
#trans = np.vectorize(lambda s: 1 if s > THRESH_MIN else 0)
trans = np.vectorize(lambda s: s)
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
