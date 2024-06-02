import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

# Given specifications
M = 32  # Filter length
fp1 = 0.2  # Passband edge frequency 1 (normalized, Nyquist = 1)
fp2 = 0.35  # Passband edge frequency 2 (normalized, Nyquist = 1)
fs1 = 0.1  # Stopband edge frequency 1 (normalized, Nyquist = 1)
fs2 = 0.425  # Stopband edge frequency 2 (normalized, Nyquist = 1)

# Ideal impulse response of a bandpass filter
def ideal_bandpass(fp1, fp2, M):
    n = np.arange(0, M)
    h_bp = np.sinc(2 * fp2 * (n - (M - 1) / 2)) - np.sinc(2 * fp1 * (n - (M - 1) / 2))
    return h_bp

# Design the ideal bandpass filter
h_ideal = ideal_bandpass(fp1, fp2, M)

# Apply Hamming window
window = np.hamming(M)
h_bandpass = h_ideal * window

# Normalize the filter coefficients
h_bandpass /= np.sum(h_bandpass)

# Frequency response of the filter
w, h = freqz(h_bandpass, worN=8000)

# Plot the magnitude response
plt.figure(figsize=(14, 7))
plt.plot(w / np.pi, np.abs(h), 'b')
plt.title('Bandpass Filter Frequency Response')
plt.xlabel('Normalized Frequency (×π rad/sample)')
plt.ylabel('Gain')
plt.grid()
plt.axvline(fp1, color='green')  # Passband edge 1
plt.axvline(fp2, color='green')  # Passband edge 2
plt.axvline(fs1, color='red')  # Stopband edge 1
plt.axvline(fs2, color='red')  # Stopband edge 2
plt.show()

# Plot the impulse response
plt.figure(figsize=(14, 7))
plt.stem(h_bandpass, use_line_collection=True)
plt.title('Impulse Response of the Bandpass Filter')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.grid()
plt.show()
