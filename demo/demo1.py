# age = 10
# print("我的年龄：%d岁" % age)
#
# '''
# 多参数占位符
# '''
# name = "张三"
# city = '广州'
# print("我叫：%s，我来自%s" % (name, city))

# '''
# python 输入
# type() 方法，查看变量的类型
# '''
# password = input("请输入密码：")
# print("刚刚您输入的密码是：", password)
# print(type(password))

# '''
# if 语句
# '''
# score = 80
# if score >= 90:
#     print("本次考试，等级为: A")
# elif 80 <= score < 90:
#     print("本次考试，等级为: B")
# elif score >= 70 and score < 80:
#     print("本次考试，等级为: C")
# elif score >= 60 and score < 70:
#     print("本次考试，等级为: D")
# else:
#     print("本次考试，等级为: E")

# '''
# 导入随机数包
# '''
# import random
# # 生成随机数，范围 0 - 5【包含0和5】
# x = random.randint(0, 5)
# print(x)


# '''
# for 语句
# '''
# for i in range(5):
#     print(i)

# for i in range(0, 10, 3):  # 从0开始，到10结束，步进值3
#     print(i)

# name = "chengdu"
# for x in name:
#     print(x, end="\t")

# arr = ['aa', 'bb', 'cc', 'dd']
# for i in range(len(arr)):
#     print(i, arr[i])

# for x in arr:
#     print(x, end='\t')

# '''
# while 语句
# '''
# i = 0
# while i < 5:
#     print("当前是第%d次循环" % i)
#     print("i == ", i)
#     i += 1

# '''
# 1-100求和
# '''
# i = 1
# result = 0
# while i <= 100:
#     result += i
#     i += 1
# print(result)

# '''
# while 后可接 else
# '''
# n = 1
# while n < 5:
#     print(n, "小于 5")
#     n += 1
# else:
#     print(n, "大于或等于 5")


# import urllib.request
# r = urllib.request.urlopen(url="https://www.baidu.com/")
# print(r)

import requests

# 添加请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}
r = requests.get("https://movie.douban.com/top250?start=0", headers=headers)
r.encoding = 'utf-8'
print(r.text)
