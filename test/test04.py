import numpy as np

arr = np.arange(1, 17).reshape((2, 2, 4))
arr2 = np.arange(18, 34).reshape((2, 2, 4))
print(arr)
print(arr2)
print(arr + arr2)
print(np.subtract(arr, arr2))
print(np.multiply(arr, arr2))
print(np.divide(arr, arr2))
