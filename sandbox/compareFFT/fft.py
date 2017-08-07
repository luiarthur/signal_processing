import numpy as np
import time

n = 1E7
x = np.arange(n)
y = np.fft.fft(x)

start = time.time() 
y = np.fft.fft(x)
print time.time() - start

print y[123456]
