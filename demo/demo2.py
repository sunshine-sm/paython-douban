"""
九九乘法表 - 打印在控制台
"""
for i in range(1, 10):
    for j in range(1, 10):
        if j == i:
            print(str(j) + " * " + str(i) + " = " + str(i * j))
            break
        else:
            print(str(j) + " * " + str(i) + " = " + str(i * j), end="\t")
