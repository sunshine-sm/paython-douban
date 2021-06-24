"""
空菱形
"""

lenth = 13  # 行数（奇数，偶数默认+1）
for i in range(0, int(lenth / 2) + 1):
    for j in range(1, 100):
        if j == lenth - i or j == lenth + i:
            print("*", end="")
        elif j > lenth + i:
            print()
            break
        else:
            print(" ", end="")
for i in range(int(lenth / 2) - 1, -1, -1):
    for j in range(1, 100):
        if j == lenth - i or j == lenth + i:
            print("*", end="")
        elif j > lenth + i:
            print()
            break
        else:
            print(" ", end="")
