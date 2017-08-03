import os
import numpy as np
from scipy.io import wavfile
from scipy import signal
import matplotlib.pyplot as plt
from notes import pitch
### Find unique elements in list (maintaining original order)
from collections import OrderedDict

HOME = os.path.expanduser('~')

### Pitch Sets
p_set = np.array(list(OrderedDict.fromkeys( pitch(np.arange(28,4188)) ))) 

### Read a wavfile
(fs, x) = wavfile.read(HOME+"/wav/embraceableYou.wav")
if x.ndim > 1: x = x[:,1]

#w_size = 2048
w_size = 4096
f, t, Zxx = signal.spectrogram(x, fs, nperseg=w_size, window=signal.get_window('blackman', w_size))

F_MAX = 4188
f_imax = np.argmin(f <= F_MAX)
f = f[:f_imax]
Zxx = Zxx[:f_imax,:]
Z = np.log(Zxx / Zxx.max())

### Plot Spectrogram
#plt.pcolormesh(t, f, Z, vmin=-10, vmax=0)
#plt.title('STFT Magnitude')
#plt.ylabel('Frequency [Hz]')
#plt.ylim([0, 4400])
#plt.xlabel('Time [sec]')
#plt.show()


### Pitch at freq
p = pitch(f + 1E-6)

### Time Chunk
tt = 4000

### Plot spectrogram at time tt:
plt.plot(f, np.exp(Z[:, tt]))
#plt.xticks(np.linspace(27, 4187, 88), p_set.tolist(), rotation=90)
plt.show()


d = {}
for z in zip(p, Z[:,tt]):
    if d.has_key(z[0]): d[z[0]] += [z[1]]
    else: d[z[0]] = [z[1]]

def compI(k):
    #trans = map(lambda dk: -np.inf if dk < -10 else dk, d[k])
    trans = d[k]
    #return np.max(trans)
    #return np.mean(trans)
    return np.median(trans)


p0, a0 = zip(*map(lambda k: (k,compI(k)), d))
#a0 = (a0 - min(a0)) / (max(a0) - min(a0))

def find_pos(k):
    pos = np.argwhere(p_set == k)
    if pos.shape[0] == 0:
        return 0
    else:
        return np.asscalar(pos) + 1

idx = map(find_pos, d)
order = np.argsort(idx)

### Pitch Detection with Keyboard Notes at bottom
#plt.figure(figsize=(20,10))
plt.plot(range(len(idx)), np.exp(a0)[order])
#plt.ylim([-10,0])
plt.xticks(range(89), [''] + p_set.tolist(), rotation=90)
plt.tight_layout()
plt.show()

