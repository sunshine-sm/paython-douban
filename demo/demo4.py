"""
等腰三角形
"""

line = 5
start = 10
for i in range(0, line):
    for j in range(0, start + line):
        if start - i <= j <= start + i:
            if start + i == j:
                print("*")
                break
            else:
                print("*", end="")
        else:
            print(" ", end="")
