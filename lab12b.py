import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Define the numerator and denominator polynomials
numerator_coeffs = [4, 8, 10]  # Coefficients of N(s) = 4s^2 + 8s + 10
denominator_coeffs = [2, 8, 18, 20]  # Coefficients of D(s) = 2s^3 + 8s^2 + 18s + 20

# Create the transfer function
system = signal.TransferFunction(numerator_coeffs, denominator_coeffs)

# Find the zeros and poles
zeros = np.roots(numerator_coeffs)
poles = np.roots(denominator_coeffs)

# Print zeros and poles
print("Zeros:", zeros)
print("Poles:", poles)

# Plot poles and zeros
plt.figure()
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
