"""
九九乘法表 - 导入到Excel
"""

import xlwt

workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet("九九乘法表")
for i in range(0, 9):
    for j in range(0, 9):
        if j >= i:
            worksheet.write(j, i, str(i + 1) + ' * ' + str(j + 1) + ' = ' + str((i + 1) * (j + 1)))

workbook.save("九九乘法表.xls")
