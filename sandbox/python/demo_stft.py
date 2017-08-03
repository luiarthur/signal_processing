import os, sys
import numpy as np
from scipy.signal import get_window
import matplotlib.pyplot as plt

HOME = os.path.expanduser('~')
sys.path.append("../../sms-tools/software/models/")

import utilFunctions as UF
import stft as STFT

### Read a wavfile
(fs, x) = UF.wavread(HOME+"/wav/embraceableYou_mono.wav")



mX, pX = STFT.stftAnal(x=x[:len(x)/10], w=get_window('blackman', Nx=801), N=4096, H=400)

plt.pcolormesh(mX.T) 
plt.show()
