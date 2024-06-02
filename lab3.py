import numpy as np
import matplotlib.pyplot as plt

# Define the original continuous-time signal
def original_signal(t):
    return 0.25 + 2 * np.sin(2 * np.pi * 5 * t) + np.sin(2 * np.pi * 12.5 * t) + 1.5 * np.sin(2 * np.pi * 20 * t) + 0.5 * np.sin(2 * np.pi * 35 * t)

# Parameters
fs = 100  # Sampling frequency (Hz)
T = 1/fs  # Sampling period (s)
t_max = 1  # Duration of the signal (s)
t = np.arange(0, t_max, T)  # Time vector for sampling
signal_continuous = original_signal(np.linspace(0, t_max, 1000))  # Continuous signal for comparison

# Sampling
signal_sampled = original_signal(t)

# Quantization
num_bits = 3  # Number of bits for quantization
num_levels = 2**num_bits  # Number of quantization levels
signal_min = np.min(signal_sampled)
signal_max = np.max(signal_sampled)
quantization_levels = np.linspace(signal_min, signal_max, num_levels)
quantized_indices = np.digitize(signal_sampled, quantization_levels) - 1
quantized_signal = quantization_levels[quantized_indices]

# Coding (Binary representation)
def int_to_binary(n, bits):
    return bin(n)[2:].zfill(bits)

coded_signal = [int_to_binary(index, num_bits) for index in quantized_indices]

# Plotting the results
plt.figure(figsize=(15, 10))

plt.subplot(3, 1, 1)
plt.plot(np.linspace(0, t_max, 1000), signal_continuous, label='Continuous Signal')
plt.stem(t, signal_sampled, linefmt='r-', markerfmt='ro', basefmt='r-', label='Sampled Signal')
plt.title('Sampling')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()

plt.subplot(3, 1, 2)
plt.stem(t, signal_sampled, linefmt='r-', markerfmt='ro', basefmt='r-', label='Sampled Signal')
plt.stem(t, quantized_signal, linefmt='g-', markerfmt='go', basefmt='g-', label='Quantized Signal')
plt.title('Quantization')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()

plt.subplot(3, 1, 3)
for i, (time, code) in enumerate(zip(t, coded_signal)):
    plt.text(time, quantized_signal[i], code, verticalalignment='bottom', horizontalalignment='right')
plt.stem(t, quantized_signal, linefmt='g-', markerfmt='go', basefmt='g-', label='Quantized Signal')
plt.title('Coding')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()

plt.tight_layout()
plt.show()

# Printing the coded signal
print("Coded Signal:")
for time, code in zip(t, coded_signal):
    print(f"Time {time:.2f}s: {code}")
