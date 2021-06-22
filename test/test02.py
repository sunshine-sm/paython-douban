import numpy as np

x = np.arange(-4, 4, 0.5)
print(x)
x2 = x.reshape(4, 4)
print(x2)
print(x2.ndim)
print(x2.shape)
print(x2.size)
print(x2.dtype)
print(x2.itemsize)
