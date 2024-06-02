import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import iirnotch, lfilter

# Define parameters
fs = 100  # Sampling rate in Hz
t = np.arange(0, 1.0, 1.0 / fs)  # Time vector for 100 samples, 1 second duration

# Generate the signal with three sinusoidal components (5 Hz, 15 Hz, 30 Hz)
s = np.sin(2 * np.pi * 5 * t) + np.sin(2 * np.pi * 15 * t) + np.sin(2 * np.pi * 30 * t)

# Plot the original signal
plt.figure(figsize=(14, 6))
plt.plot(t, s, label='Original Signal')
plt.title('Original Signal in Time Domain')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()
plt.show()

# Design IIR notch filters to suppress 5 Hz and 30 Hz frequencies
def design_notch_filter(freq, fs, Q=30):
    w0 = freq / (fs / 2)  # Normalized frequency
    b, a = iirnotch(w0, Q)
    return b, a

# Notch filter for 5 Hz
b1, a1 = design_notch_filter(5, fs)

# Notch filter for 30 Hz
b2, a2 = design_notch_filter(30, fs)

# Apply notch filters
s_filtered = lfilter(b1, a1, s)
s_filtered = lfilter(b2, a2, s_filtered)

# Plot the filtered signal
plt.figure(figsize=(14, 6))
plt.plot(t, s_filtered, label='Filtered Signal')
plt.title('Filtered Signal in Time Domain')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()
plt.show()
