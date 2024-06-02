import numpy as np
import matplotlib.pyplot as plt

def DFT(x):
    """
    Compute the Discrete Fourier Transform of the 1D array x
    """
    N = len(x)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
    return X

def IDFT(X):
    """
    Compute the Inverse Discrete Fourier Transform of the 1D array X
    """
    N = len(X)
    x = np.zeros(N, dtype=complex)
    for n in range(N):
        for k in range(N):
            x[n] += X[k] * np.exp(2j * np.pi * k * n / N)
    return x / N

# Define the signal
N = 1000  # Length of the signal
t = np.linspace(0, 1, N, endpoint=False)  # Time vector
f = 0.25 + 2 * np.sin(2 * np.pi * 5 * t) + np.sin(2 * np.pi * 12.5 * t) + 1.5 * np.sin(2 * np.pi * 20 * t) + 0.5 * np.sin(2 * np.pi * 35 * t)

# Compute the DFT
F = DFT(f)

# Compute the IDFT
f_reconstructed = IDFT(F)

# Plot the original and reconstructed signals
plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.plot(t, f)
plt.title('Original Time Domain Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 2)
frequencies = np.fft.fftfreq(N, d=1/N)
plt.stem(frequencies[:N//2], np.abs(F[:N//2]), 'b', markerfmt=" ", basefmt="-b")
plt.title('DFT - Amplitude Spectrum')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 3)
plt.plot(t, f_reconstructed.real)
plt.title('Reconstructed Time Domain Signal from IDFT')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
