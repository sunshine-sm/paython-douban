import numpy as np

x = np.arange(-4, 4, 0.5)
x.resize(4, 4)
print(x)
x2 = x.ravel()
print(x2)
x3 = x.reshape(4, 2, 2)
print(x3)
x4 = x3.transpose(1, 0, 2)
print(x4)
x5 = x3.reshape(2, 4, 2)
print(x5)
