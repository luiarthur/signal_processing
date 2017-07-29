import os
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

HOME = os.path.expanduser('~')

### Read a wavfile
(fs, x) = wavfile.read(HOME+"/tmp/embrace.wav")

### Write a wavfile
#wavfile.write('bla.wav', fs, y)

### Get the duration of the file
seconds_duration_of_file = x.shape[0] / float(fs) 

### Get the 
x.shape # 2 columns because stereo (L, R)

### Sampled Wave (every 500)
xs = x[::500,0]

### Get the time index (also sampled every 500)
t = (np.arange(0,x.shape[0],500) / float(fs)) / 60 # minutes


### Plot the wave
plt.plot(t, xs) # get every 500
plt.show()
