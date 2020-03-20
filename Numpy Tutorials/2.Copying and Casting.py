"""Similar to Python lists, when we make a reference to a NumPy array it doesn't create a different array. 
Therefore, if we change a value using the reference variable, it changes the original array as well. 
We get around this by using an array's inherent copy function. 
The function has no required arguments, and it returns the copied array."""

"""In the code example below, c is a reference to a while d is a copy.
Therefore, changing c leads to the same change in a, while changing d does not change the value of b."""
#Copying

import numpy as np
a = np.array([0, 1])
b = np.array([9, 8])
c = a
print('Array a: {}'.format(repr(a)))
c[0] = 5
print('Array a: {}'.format(repr(a)))

d = b.copy()
d[0] = 6
print('Array b: {}'.format(repr(b)))

#Casting
"""We cast NumPy arrays through their inherent astype function.
 The function's required argument is the new type for the array. 
 It returns the array cast to the new type."""

"""The code below shows an example of casting using the astype function.
 The dtype property returns the type of an array."""
arr = np.array([0, 1, 2])
print(arr.dtype)
arr = arr.astype(np.float32)
print(arr.dtype)


#NaN
"""When we don't want a NumPy array to contain a value at a particular index,
 we can use np.nan to act as a placeholder.
 A common usage for np.nan is as a filler value for incomplete data.

The code below shows an example usage of np.nan. Note that np.nan cannot take on an integer type."""

arr = np.array([np.nan, 1, 2])
print(repr(arr))

arr = np.array([np.nan, 'abc'])
print(repr(arr))

# Will result in a ValueError
np.array([np.nan, 1, 2], dtype=np.int32)



#Infinity
"""To represent infinity in NumPy, we use the np.inf special value.
 We can also represent negative infinity with -np.inf.

The code below shows an example usage of np.inf. Note that np.inf cannot take on an integer type."""

print(np.inf > 1000000)

arr = np.array([np.inf, 5])
print(repr(arr))

arr = np.array([-np.inf, 1])
print(repr(arr))

# Will result in an OverflowError
np.array([np.inf, 3], dtype=np.int32)


