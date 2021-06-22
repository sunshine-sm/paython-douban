import matplotlib.pyplot as plt
import numpy as np
import math

plt.rcParams['font.sans-serif']='SimHei'
fig = plt.figure(figsize=[6, 4], facecolor='#F0FFF0', num='金融数据分析',
                 edgecolor='#FFD700', frameon=True, linewidth=8)
m1 = plt.subplot(2, 2, 1)
m2 = plt.subplot(2, 2, 2)
m3 = plt.subplot(2, 2, 3)
m4 = plt.subplot(2, 2, 4)
x = np.random.randint(1, 100, 100)
bin = np.arange(1, 100, 10)
m1.hist(x, bin, color='r')
labels = ['娱乐', '育儿', '饮食', '房贷', '交通', '其他']
sizes = np.random.randint(1, 100, 6)
m2.pie(sizes, labels=labels, shadow=True, startangle=150,
       autopct='%1.1f%%')
m3.specgram(np.random.randn(3000), NFFT=200, Fs=100, noverlap=100)
x = np.random.randint(1, 100, 10)
y1 = np.random.randint(1, 100, 10)
y2 = np.random.randint(1, 100, 10)
y3 = np.random.randint(1, 100, 10)
colors = ['#EED5D2', '#FF34B3', '#836FFF']
m4.stackplot(x, y1, y2, y3, labels=[y1, y2, y3], colors=colors)
plt.show()