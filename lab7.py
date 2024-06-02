import numpy as np
import matplotlib.pyplot as plt

# Define the sequence x(n)
x = np.array([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1])
n = np.arange(len(x))  # Index array

# Define the length of the new sequence y(n) to handle shifts
y_length = len(x) + 9  # Because the shifts range from -4 to 5
y = np.zeros(y_length)
n_y = np.arange(-4, len(x) + 5)  # Index array for y(n)

# Shifted and scaled versions of x(n)
x_shifted_minus_5 = np.zeros(y_length)
x_shifted_plus_4 = np.zeros(y_length)

# Applying shifts
x_shifted_minus_5[5:len(x) + 5] = x
x_shifted_plus_4[:len(x)] = x

# Compute y(n) = 2x(n - 5) - 3x(n + 4)
y = 2 * x_shifted_minus_5 - 3 * x_shifted_plus_4

# Plot the sequences
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.stem(n, x)
plt.title('Sequence x(n)')
plt.xlabel('n')
plt.ylabel('x[n]')

plt.subplot(3, 1, 2)
plt.stem(n_y, 2 * x_shifted_minus_5, 'r')
plt.title('Sequence 2x(n - 5)')
plt.xlabel('n')
plt.ylabel('2x[n-5]')

plt.subplot(3, 1, 3)
plt.stem(n_y, -3 * x_shifted_plus_4, 'g')
plt.title('Sequence -3x(n + 4)')
plt.xlabel('n')
plt.ylabel('-3x[n+4]')

plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 4))
plt.stem(n_y, y)
plt.title('Sequence y(n) = 2x(n - 5) - 3x(n + 4)')
plt.xlabel('n')
plt.ylabel('y[n]')

plt.tight_layout()
plt.show()

# Print the sequences
print("Sequence x(n):", x)
print("Sequence y(n):", y)
