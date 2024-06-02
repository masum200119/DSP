import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display

# Load the speech signal
file_path = 'path_to_your_speech_file.wav'  # Replace with your file path
signal, sr = librosa.load(file_path, sr=None)

# Define frame parameters
frame_size = 0.025  # 25 ms
frame_stride = 0.010  # 10 ms
frame_length = int(frame_size * sr)
frame_step = int(frame_stride * sr)

# Normalize the signal
signal = signal / np.max(np.abs(signal))

# Compute short-time energy
def short_time_energy(signal, frame_length, frame_step):
    energy = []
    for i in range(0, len(signal) - frame_length, frame_step):
        frame = signal[i:i + frame_length]
        energy.append(sum(frame ** 2))
    return np.array(energy)

# Compute zero-crossing rate (ZCR)
def zero_crossing_rate(signal, frame_length, frame_step):
    zcr = []
    for i in range(0, len(signal) - frame_length, frame_step):
        frame = signal[i:i + frame_length]
        zcr.append(sum(librosa.zero_crossings(frame, pad=False)))
    return np.array(zcr)

# Calculate energy and ZCR
energy = short_time_energy(signal, frame_length, frame_step)
zcr = zero_crossing_rate(signal, frame_length, frame_step)

# Define thresholds for voiced/unvoiced/silence detection
energy_threshold = np.max(energy) * 0.1
zcr_threshold = np.mean(zcr)

# Segment the signal
voiced_frames = (energy > energy_threshold) & (zcr < zcr_threshold)
unvoiced_frames = (energy > energy_threshold) & (zcr >= zcr_threshold)
silence_frames = energy <= energy_threshold

# Generate time axes
time_signal = np.linspace(0, len(signal) / sr, num=len(signal))
time_frames = np.linspace(0, len(signal) / sr, num=len(energy))

# Plot the signal and mark regions
plt.figure(figsize=(14, 8))
plt.subplot(2, 1, 1)
plt.plot(time_signal, signal, label='Speech Signal')
plt.title('Speech Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# Highlight voiced regions
for i, frame in enumerate(voiced_frames):
    if frame:
        plt.axvspan(time_frames[i] - frame_stride / 2, time_frames[i] + frame_stride / 2, color='green', alpha=0.5, label='Voiced' if i == 0 else "")

# Highlight unvoiced regions
for i, frame in enumerate(unvoiced_frames):
    if frame:
        plt.axvspan(time_frames[i] - frame_stride / 2, time_frames[i] + frame_stride / 2, color='yellow', alpha=0.5, label='Unvoiced' if i == 0 else "")

# Highlight silence regions
for i, frame in enumerate(silence_frames):
    if frame:
        plt.axvspan(time_frames[i] - frame_stride / 2, time_frames[i] + frame_stride / 2, color='red', alpha=0.5, label='Silence' if i == 0 else "")

plt.legend(loc='upper right')
plt.subplot(2, 1, 2)
plt.plot(time_frames, energy, label='Short-Time Energy')
plt.plot(time_frames, zcr, label='Zero-Crossing Rate')
plt.title('Energy and Zero-Crossing Rate')
plt.xlabel('Time (s)')
plt.ylabel('Magnitude')
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()
