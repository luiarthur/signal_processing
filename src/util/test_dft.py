import numpy as np
import dft
import matplotlib.pyplot as plt

reload(dft)

### Params
N = 64
k0 = 7.5

### Signal
x = np.exp(1j * 2 * np.pi * k0 / N * np.arange(N))
y = np.cos(2 * np.pi * k0 / N * np.arange(N))


### DFT
sx = dft.dft(x,center=False) # SLOW
fftx = np.fft.fft(x)

sy = dft.dft(y, center=False) # SLOW
ffty = np.fft.fft(y)

### Assert that the ifft of fft is itself
assert all(np.abs(x - np.fft.ifft(fftx)) < 1E-10)

### Plot the DFT
plt.plot(np.abs(sx)) # Shows peak of N at k0
plt.plot(np.abs(sy)) # Shows two peaks (symmetric)
plt.show()

### Plot FFT
plt.plot(np.abs(fftx)) # Shows peak of N at k0
plt.plot(np.abs(ffty)) # Shows two peaks (symmetric)
plt.show()


### Plot the signal
plt.plot(np.imag(x))
plt.plot(np.real(x))
plt.show()

plt.plot(y)
plt.show()

### Check the the inverse of a dft is itself
plt.plot(np.real(x) - dft.idft(sx))
plt.ylim([-1,1])
plt.show()

### Energy Conservation
assert np.mean(np.abs(sx) ** 2) - np.sum(np.abs(x) ** 2) < 1E-5
assert np.mean(np.abs(sy) ** 2) - np.sum(np.abs(y) ** 2) < 1E-5

