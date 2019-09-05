import numpy as np
from scipy.special import factorial

arr1d = np.arange(12)
arr2d = [[1,2,3],[6,5,4]]

print(arr1d)
print(arr2d)

s = arr1d[4:7]
s[1] = 0

print(arr1d)
print(s)

arr2d = factorial(arr2d,exact=True )
print(arr2d)