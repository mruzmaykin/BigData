import numpy as np
from scipy.special import factorial

arr1d = np.arange(12)
arr2d = [[1,2,3],[6,5,4]]


print("=================================")
print("Part 1.")
print("Arr1d:\n",arr1d)
print("Arr2d:\n",arr2d)
s = arr1d[4:7]
s[1] = 0

print("=================================")
print("Part 2.")
print("Arr1d:\n",arr1d)
print("Slice s:\n",s)

print("=================================")

arr2d = factorial(arr2d,exact=True )
print("Part 3.")
print("Factorialized Arr2d:\n",arr2d)

print("=================================")