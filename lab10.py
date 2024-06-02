import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

# Specifications
fs = 10000  # Sampling frequency in Hz
f_pass = 1500  # Passband edge in Hz
transition_width = 500  # Transition width in Hz
N = 67  # Filter length

# Calculate the normalized cutoff frequency
f_cutoff = f_pass + transition_width / 2
normalized_cutoff = f_cutoff / (fs / 2)

# Generate the ideal lowpass filter (sinc function)
n = np.arange(N)
h_ideal = np.sinc(2 * normalized_cutoff * (n - (N - 1) / 2))

# Apply the Blackman window
blackman_window = np.blackman(N)
h = h_ideal * blackman_window

# Normalize the filter coefficients
h = h / np.sum(h)

# Frequency response
w, H = freqz(h, worN=8000)
frequencies = w * fs / (2 * np.pi)

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
