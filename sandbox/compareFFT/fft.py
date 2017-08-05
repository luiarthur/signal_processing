import numpy as np
import time

n = 1E7
x = np.arange(n)

start = time.time() 
y = np.fft.fft(x)
print time.time() - start
