import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Define the numerator and denominator polynomials
numerator_coeffs = [1, 0, 0, 1]  # Coefficients of N(s) = s^3 + 1
denominator_coeffs = [1, 0, 2, 0, 1]  # Coefficients of D(s) = s^4 + 2s^2 + 1

# Create the transfer function
system = signal.TransferFunction(numerator_coeffs, denominator_coeffs)

# Find the zeros (roots of the numerator) and poles (roots of the denominator)
zeros = np.roots(numerator_coeffs)
poles = np.roots(denominator_coeffs)

# Print zeros and poles
print("Zeros:", zeros)
print("Poles:", poles)

# Plot the zeros and poles
plt.figure(figsize=(10, 6))
plt.scatter(np.real(zeros), np.imag(zeros), marker='o', color='r', label='Zeros')
plt.scatter(np.real(poles), np.imag(poles), marker='x', color='b', label='Poles')
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.grid()
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.title('Poles and Zeros Plot')
plt.legend()
plt.show()
