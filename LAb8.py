import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

# Given specifications
fs = 20000  # Sampling frequency in Hz
passband_edge = 2000  # Passband edge in Hz
stopband_edge = 5000  # Stopband edge in Hz
filter_length = 21  # Length of the filter

# Normalized frequencies
passband_edge_normalized = passband_edge / (fs / 2)
stopband_edge_normalized = stopband_edge / (fs / 2)

# Ideal impulse response of the low-pass filter
def ideal_lp(cutoff_freq, num_taps):
    M = num_taps - 1
    n = np.arange(0, num_taps)
    h = np.sinc(2 * cutoff_freq * (n - M / 2))
    return h

# Design the band-pass filter
h_low = ideal_lp(stopband_edge_normalized, filter_length)
h_high = ideal_lp(passband_edge_normalized, filter_length)
h_bandpass = h_low - h_high

# Apply Hanning window
window = np.hanning(filter_length)
h_bandpass_windowed = h_bandpass * window

# Normalize the filter coefficients
h_bandpass_windowed /= np.sum(h_bandpass_windowed)

# Frequency response of the filter
w, h = freqz(h_bandpass_windowed, worN=8000)

# Plot the magnitude response
plt.figure(figsize=(14, 7))
plt.plot(0.5 * fs * w / np.pi, np.abs(h), 'b')
plt.title('Bandpass Filter Frequency Response')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain')
plt.grid()
plt.axvline(passband_edge, color='green')  # Passband edge
plt.axvline(stopband_edge, color='red')  # Stopband edge
plt.show()
