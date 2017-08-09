#import wave

import os
import numpy as np
from scipy.io import wavfile
from scipy import signal
import matplotlib.pyplot as plt
from notes import pitch, piano_freq
### Find unique elements in list (maintaining original order)
from collections import OrderedDict

HOME = os.path.expanduser('~')

### Pitch Sets
#p_set = np.array(list(OrderedDict.fromkeys( pitch(np.arange(28,4188)) ))) 
f_set = piano_freq #np.linspace(27.5, 4186, num=88)
p_set = pitch(f_set)

### Read a wavfile
(fs, x) = wavfile.read(HOME+"/wav/embraceableYou.wav")
if x.ndim > 1: x = x[:,1]

#w_size = 2048
#w_size = 4096 * 2
#w_size = 4096 * 4
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

def getTimeChunk(s, t):
    return np.argmin( np.abs(t - s) )


### Pitch at freq
p = pitch(f + 1E-6)

### Time Chunk
#tt = 1000
#tt = 500
tt = getTimeChunk(14.8, t)
#tt = getTimeChunk(15, t)

### Plot spectrogram at time tt:

### Normalized
#z = np.exp(Z[:,tt] - Z[:,tt].max()) / np.exp(Z[:,tt] - Z[:,tt].max()).sum()
#plt.plot(f, z)
#plt.show()

### Scaled to 0,1
z = np.exp(Z[:,tt] - Z[:,tt].max())
#z = np.exp( np.log(Zxx[:,tt]) - np.log(Zxx[:,tt].max()) )
plt.plot(f, z)
plt.show()

### UnNormalized
#plt.plot(f, np.exp(Z[:, tt]))
#plt.xticks(np.linspace(27, 4187, 88), p_set.tolist(), rotation=90)
#plt.show()


d = {}
for k in p_set:
    d[k] = []

for z in zip(p, Z[:,tt]):
    if d.has_key(z[0]): d[z[0]] += [z[1]]

for k in d:
    if d[k] == []: d[k] = [-np.inf]

def compI(k):
    #trans = map(lambda dk: -np.inf if dk < -10 else dk, d[k])
    trans = d[k]
    #return np.min(trans)
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
zz = np.array(a0)[order]

thresh = .2
norm_z = np.exp(zz - zz.max())
note_idx =  np.argwhere( norm_z > thresh).T[0]
note_guess = p_set[ note_idx ]

### Pitch Detection with Keyboard Notes at bottom
#plt.figure(figsize=(20,10))
#plt.plot(range(len(idx)), np.exp(zz))
plt.plot(range(len(idx)), norm_z)
#plt.ylim([-10,0])
plt.xticks(range(88), p_set.tolist(), rotation=90)
plt.axhline(y=thresh, color='grey')

for i in note_idx:
    plt.axvline(x=i, color='orange')

plt.tight_layout()
plt.show()

### Movie
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ln, = plt.plot([], [], animated=True)
title = ax.text(.8, .95, '', transform = ax.transAxes, va='center')
plt.xticks(np.log(f_set), p_set, rotation=90)

def init():
    ax.set_xlim(np.log(f_set[0])-.1, np.log(f_set[-1])+.1)
    #ax.set_ylim(0, 1.1)
    #ax.set_ylim(0, .01)
    ax.set_ylim(0, 1.1)
    return [ln, title]

def update(i):
    #ydata = np.exp( np.log(Zxx[:,i]) - np.log(Zxx[:,i].max()) )
    #ydata = np.exp( np.log(Zxx[:,i]) - np.log(Zxx.max()) )
    ydata = np.exp( np.log(Zxx[:,i]) - np.log(10000) )
    ln.set_data(np.log(f), ydata)
    title.set_text("time: " + str(np.round(t[i],2)) + "s")
    return [title, ln]

delay = (t[1:] - t[:-1]).mean() * 1000

ani = FuncAnimation(fig, update, frames=range(t.size),
                    init_func=init, blit=True, repeat=False, interval=delay)

#anim_running = True

#def onClick(event):
#    global anim_running
#    if anim_running:
#        anim.event_source.stop()
#        anim_running = False
#    else:
#        anim.event_source.start()
#        anim_running = True

plt.show()

