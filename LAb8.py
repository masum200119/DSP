import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

# Specifications
Fs = 20000  # Sampling frequency in Hz
F_pass = 2000  # Passband edge in Hz
F_stop = 5000  # Stopband edge in Hz
N = 21  # Filter length

# Calculate the normalized cutoff frequency
F_cutoff = (F_pass + F_stop) / 2
normalized_cutoff = F_cutoff / (Fs / 2)

# Generate the ideal lowpass filter (sinc function)
n = np.arange(N)
h_ideal = np.sinc(2 * normalized_cutoff * (n - (N - 1) / 2))

# Apply the Hanning window
hanning_window = np.hanning(N)
h = h_ideal * hanning_window

# Normalize the filter coefficients
h = h / np.sum(h)

# Frequency response
w, H = freqz(h, worN=8000)
frequencies = w * Fs / (2 * np.pi)

# Plot the impulse response
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.stem(n, h)
plt.title('Impulse Response')
plt.xlabel('Samples')
plt.ylabel('Amplitude')

# Plot the frequency response
plt.subplot(2, 1, 2)
plt.plot(frequencies, 20 * np.log10(abs(H)))
plt.title('Frequency Response')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.grid()
plt.ylim([-100, 5])

plt.tight_layout()
plt.show()
