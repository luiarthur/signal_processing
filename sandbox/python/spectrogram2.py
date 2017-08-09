import os
import numpy as np
from scipy.io import wavfile
from scipy import signal
import matplotlib.pyplot as plt
from notes import pitch, piano_freq, freq_dict, bin_spec

HOME = os.path.expanduser('~')

### Read a wavfile
(fs, x) = wavfile.read(HOME+"/wav/embraceableYou.wav")
if x.ndim > 1: x = x[:,1]

w_size = 4096
f, t, Zxx = signal.spectrogram(x, fs, nperseg=w_size, window=signal.get_window('blackman', Nx=w_size))
f, t, Zxx = bin_spec(f, t, Zxx)

### Plot Spectrogram
plt.pcolormesh(t, f, Zxx, vmin=.0001, vmax=.0005)
plt.title('STFT Magnitude')
plt.ylabel('Frequency [Hz]')
plt.ylim([0, 4200])
plt.xlabel('Time [sec]')
plt.yticks(f, pitch(f))
plt.show()


### Movie
from matplotlib.animation import FuncAnimation

#thresh = .0005
thresh = .5
fig, ax = plt.subplots()
ln, = plt.plot([], [], animated=True)
title = ax.text(.8, .95, '', transform = ax.transAxes, va='center')
#plt.xticks(np.log(piano_freq), pitch(piano_freq), rotation=90)
plt.xticks(np.log(f), pitch(f), rotation=90)
plt.axhline(y=thresh, color='grey')

def init():
    #ax.set_ylim(0, 1.1)
    #ax.set_ylim(0, .01)
    #ax.set_ylim(0, 1.1)
    ax.set_ylim(0, thresh*2)
    ax.set_xlim(np.log(27.5), np.log(4186))
    return [ln, title]

def update(i):
    ydata = np.exp( np.log(Zxx[:,i]) - np.log(Zxx[:,i].max()) )
    #ydata = np.exp( np.log(Zxx[:,i]) - np.log(Zxx.max()) )
    #ydata = np.exp( np.log(Zxx[:,i]) - np.log(10000) )
    #ydata = Zxx[:,i]
    ln.set_data(np.log(f), ydata)
    title.set_text("time: " + str(np.round(t[i],2)) + "s")
    #print t[i], pitch(f[Zxx[:,i].argmax()])
    return [title, ln]

delay = (t[1:] - t[:-1]).mean() * 1000

ani = FuncAnimation(fig, update, frames=range(t.size),
                    init_func=init, blit=True, repeat=False, interval=delay)

plt.show()

