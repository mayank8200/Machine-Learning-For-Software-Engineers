import numpy as np  # import the NumPy library

# Initializing a NumPy array
arr = np.array([-1, 2, 5], dtype=np.float32)

# Print the representation of the array
print(repr(arr))

"""if an array input has mixed int and float elements, 
all the integers will be cast to their floating-point equivalents."""

arr1 = np.array([0, 0.1, 2])
print(repr(arr1))
