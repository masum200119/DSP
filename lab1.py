import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
sampling_rate = 1000  # Sampling rate in Hz
T = 1 / sampling_rate  # Sampling interval
L = 1000  # Length of the signal
t = np.arange(0, L) * T  # Time vector

# Define the signal
f = 0.25 + 2 * np.sin(2 * np.pi * 5 * t) + np.sin(2 * np.pi * 12.5 * t) + 1.5 * np.sin(2 * np.pi * 20 * t) + 0.5 * np.sin(2 * np.pi * 35 * t)

# Compute the FFT
F = np.fft.fft(f)
P2 = np.abs(F / L)  # Two-sided spectrum
P1 = P2[:L//2+1]  # Single-sided spectrum
P1[1:-1] = 2 * P1[1:-1]  # Because we dropped half the FFT, we multiply by 2

# Frequency axis
frequencies = sampling_rate * np.arange(0, (L/2)+1) / L

# Plot the signal
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, f)
plt.title('Time Domain Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.plot(frequencies, P1)
plt.title('Single-Sided Amplitude Spectrum of the Signal')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
