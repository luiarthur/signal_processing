import os
import numpy as np
from scipy.io import wavfile
from scipy import signal
import matplotlib.pyplot as plt
from notes import pitch, piano_freq, freq_dict, my_spectrogram


HOME = os.path.expanduser('~')

### Read a wavfile
(fs, x) = wavfile.read(HOME+"/wav/embraceableYou.wav")
if x.ndim > 1: x = x[:,1]


### Spectrogram (High resolution)
f, t, Zxx = my_spectrogram(x, fs)
f.size

### Plot Spectrogram
plt.pcolormesh(t, np.log(f+1E-6), Zxx, vmin=.05, vmax=1, cmap=plt.cm.gist_heat)
plt.title('STFT Magnitude')
plt.ylabel('Frequency [Hz]')
plt.ylim([np.log(f[1]), np.log(f.max())])
plt.xlabel('Time [sec]')
plt.yticks(np.log(f+1E-6), pitch(f))
plt.show()

### Dump Data ###
np.savetxt('out/Zxx.txt', Zxx, '%.4f')
np.savetxt('out/f.txt', f, '%.2f')
np.savetxt('out/t.txt', t, '%.2f')
