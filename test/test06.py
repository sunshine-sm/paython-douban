import math

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=[6, 4], facecolor='#F0FFF0', num='金融数据分析',
                 edgecolor='#FFD700', frameon=True, linewidth=8)
m1 = plt.subplot(2, 2, 1)
m2 = plt.subplot(2, 2, 2)
m3 = plt.subplot(2, 2, 3)
m4 = plt.subplot(2, 2, 4)
x = np.arange(0, 2 * math.pi, 0.001)
y = np.sin(x)
m1.plot(x, y)
x2 = np.arange(1, 10, 2)
y2 = 2 * x2
m2.bar(x2, y2)
m3.barh(x2, y2)
m4.scatter(x2, y2)
plt.show()
