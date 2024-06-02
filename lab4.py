import numpy as np

def convolve(x, y):
  """
  Calculates the convolution of two sequences.

  Args:
      x: A 1D NumPy array representing the first sequence.
      y: A 1D NumPy array representing the second sequence.

  Returns:
      A 1D NumPy array representing the convolution of x and y.
  """
  return np.convolve(x, y, mode='full')

def correlate(x, y):
  """
  Calculates the correlation of two sequences.

  Args:
      x: A 1D NumPy array representing the first sequence.
      y: A 1D NumPy array representing the second sequence.

  Returns:
      A 1D NumPy array representing the correlation of x and y.
  """
  # Reverse the second sequence for correlation
  y_flipped = np.flip(y)
  return np.convolve(x, y_flipped, mode='full')

# Sample sequences (replace with your own data if needed)
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

# Calculate convolution
convolution_result = convolve(x, y)
print("Convolution result:", convolution_result)

# Calculate correlation
correlation_result = correlate(x, y)
print("Correlation result:", correlation_result)
