import numpy as np

def dft(x, center=False):
    N = x.size
    if center:
        nv = np.arange(-N/2.0, N/2.0)
    else:
        nv = np.arange(N)

    s = map(lambda k: np.sum(x * np.exp(-1j * 2 * np.pi * k * nv / N)), nv)

    return s

def idft(X, center=False):
    N = len(X)

    if center:
        kv = np.arange(-N/2.0, N/2.0)
    else:
        kv = np.arange(N)

    s = map(lambda n: np.mean(X * np.exp(1j * 2 * np.pi * kv * n / N)), kv)

    return s

