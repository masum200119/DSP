import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

# Given specifications
fs = 10000  # Sampling frequency in Hz
passband_edge = 1500  # Passband edge in Hz
transition_width = 500  # Transition width in Hz
filter_length = 67  # Length of the filter

# Calculate the cutoff frequency
cutoff_freq = passband_edge + transition_width / 2

# Normalized cutoff frequency
normalized_cutoff = cutoff_freq / (fs / 2)

# Ideal impulse response of the low-pass filter
def ideal_lp(cutoff, num_taps):
    M = num_taps - 1
    n = np.arange(0, num_taps)
    h = np.sinc(2 * cutoff * (n - M / 2))
    return h

# Design the low-pass filter
h_ideal = ideal_lp(normalized_cutoff, filter_length)

# Apply Blackman window
window = np.blackman(filter_length)
h_blackman = h_ideal * window

# Normalize the filter coefficients
h_blackman /= np.sum(h_blackman)

# Frequency response of the filter
w, h = freqz(h_blackman, worN=8000)

# Plot the magnitude response
plt.figure(figsize=(14, 7))
plt.plot(0.5 * fs * w / np.pi, np.abs(h), 'b')
plt.title('Lowpass Filter Frequency Response')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain')
plt.grid()
plt.axvline(passband_edge, color='green')  # Passband edge
plt.axvline(passband_edge + transition_width, color='red')  # Start of the stopband
plt.show()

# Plot the impulse response
plt.figure(figsize=(14, 7))
plt.stem(h_blackman, use_line_collection=True)
plt.title('Impulse Response of the Lowpass Filter')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.grid()
plt.show()
