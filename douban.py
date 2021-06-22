"""
爬取 豆瓣top250电影 信息
地址：https://movie.douban.com/top250?start=0
"""

import re  # 正则表达式
import sqlite3  # 进行数据库操作

import matplotlib.pyplot as plt  # 制作图标工具
import numpy as np
import requests  # 制定URL，获取网页数据
import xlwt  # 进行Excel操作
from bs4 import BeautifulSoup  # 网页解析，获取数据

# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = ['Simhei']
# 用来正常显示符号
plt.rcParams['axes.unicode_minus'] = False

# 正则 获取 【影片详情链接】
findLink = re.compile(r'<a href="(.*?)">')
# 正则 获取 【影片图片地址】
findImg = re.compile(r'<img.*src="(.*?)"', re.S)
# 正则 获取 【影片名称】
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 正则 获取 【影片评分】
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 正则 获取 【影片评价人数】
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 正则 获取 【影片概况】
findQuote = re.compile(r'<span class="inq">(.*)</span>')
# 正则 获取 【影片相关内容】
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)
# 正则 获取 【上映年份】
findYear = re.compile(r'<br/>(.*?)/', re.S)
# 正则 获取 【国家】
findCountry = re.compile(r'<br/>.*?/(.*?)/', re.S)


# 爬取网页数据
def get_data(base_url):
    data = []
    for i in range(0, 250, 25):
        url = base_url + str(i)
        html = ask_url(url)

        # 解析数据
        soup = BeautifulSoup(html, "html.parser")
        # 查找到所有的电影节点信息
        items = soup.select("div .item")
        # 遍历节点数据
        for item in items:
            movie = {}
            # 将节点标签转为字符串
            item = str(item)
            # count = re.findall(re.compile(r'<em class="">(\d*)</em>'), item)[0]
            # print(count)
            # 获取影片名称
            titles = re.findall(findTitle, item)
            if len(titles) > 1:
                movie["ctitle"] = titles[0]
                movie["otitle"] = titles[1].replace("/", "").replace(u"\xa0", "")
            else:
                movie["ctitle"] = titles[0]
                movie["otitle"] = " "

            # 获取影片详情链接
            link = re.findall(findLink, item)[0]
            movie["link"] = link
            # 获取影片图片
            img = re.findall(findImg, item)[0]
            movie["img"] = img
            # 获取影片评分
            rating = re.findall(findRating, item)[0]
            movie["rating"] = rating
            # 获取影片评价人数
            judge = re.findall(findJudge, item)[0]
            movie["judge"] = judge
            # 获取影片概况
            quotes = re.findall(findQuote, item)
            if len(quotes) > 0:
                movie["quote"] = quotes[0]
            else:
                movie["quote"] = ""
            # 获取影片相关内容
            info = re.findall(findBd, item)[0]
            info = re.sub("<br(\s+)?/>(\s+)?", " ", info)
            movie["info"] = info.strip().replace(u"\xa0", " ")
            # 获取年份
            year = re.findall(findYear, item)[0].strip()
            movie["year"] = year[0:4]
            # 获取国家
            country = re.findall(findCountry, item)[0].strip().split(" ")[0]
            movie["country"] = country if country.find("(") < 0 else country[5:9]

            # 将影片信息保存到数组中
            data.append(movie)
    return data


# 发起请求获取数据
def ask_url(url):
    # 添加请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4549.0 Safari/537.36'
    }
    # 爬取数据
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    html = res.text
    return html


# 统计电影评分数据并储存到数据库
def count_movies_rating(movies, db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    dict = {}
    # 遍历所有影片信息
    for movie in movies:
        key = movie.get('rating')
        if dict.__contains__(key):
            dict[key] = dict[key] + 1
        else:
            dict[key] = 1
    # 遍历Map集合
    for item in dict.items():
        sql = '''insert into db_movies_rating(rating, count) values("%s", "%s")''' % (item[0], item[1])
        cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


# 统计电影年份数据并储存到数据库
def count_movies_year(movies, db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    dict = {}
    # 遍历所有影片信息
    for movie in movies:
        key = movie.get('year')
        if dict.__contains__(key):
            dict[key] = dict[key] + 1
        else:
            dict[key] = 1
    # 遍历Map集合
    for item in dict.items():
        sql = '''insert into db_movies_year(year, count) values("%s", "%s")''' % (item[0], item[1])
        cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


# 统计电影年份数据并储存到数据库
def count_movies_country(movies, db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    dict = {}
    # 遍历所有影片信息
    for movie in movies:
        key = movie.get('country')
        if dict.__contains__(key):
            dict[key] = dict[key] + 1
        else:
            dict[key] = 1
    # 遍历Map集合
    for item in dict.items():
        sql = '''insert into db_movies_country(country, count) values("%s", "%s")''' % (item[0], item[1])
        cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


# 保存所有电影数据
def save_movies(movies, db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    for movie in movies:
        sql = '''insert into db_movies(cname, oname, year, country, link, img_url, rating, judge, quote, info) values ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")''' % (
            movie['ctitle'], movie["otitle"], movie['year'], movie['country'], movie['link'], movie['img'],
            movie['rating'], movie['judge'], movie['quote'], movie['info'])
        cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


# 初始化数据库
def init_db(db_path):
    sql = '''
        -- 电影表
        drop table if exists db_movies;
        create table db_movies
        (
            id      integer primary key autoincrement not null, -- ID
            cname   text default '',                            -- 评分
            oname   text default '',                            -- 数量
            year    text default '',                            -- 年份
            country text default '',                            -- 国家
            link    text default '',                            -- 链接地址
            img_url text default '',                            -- 图片链接
            rating  real default 0,                             -- 评分
            judge   text default '',                            -- 评价人数
            quote   text default '',                            -- 影片概况
            info    text default ''                             -- 相关内容
        );
        -- 电影评分统计表
        drop table if exists db_movies_rating;
        create table db_movies_rating
        (
            id     integer primary key autoincrement not null, -- ID
            rating real    default 0 not null,                 -- 评分
            count  integer default 0 not null                  -- 数量
        );
        -- 电影年份统计表
        drop table if exists db_movies_year;
        create table db_movies_year
        (
            id     integer primary key autoincrement not null, -- ID
            year   real    default 0 not null,                 -- 年份
            count  integer default 0 not null                  -- 数量
        );
        -- 电影国家统计表
        drop table if exists db_movies_country;
        create table db_movies_country
        (
            id        integer primary key autoincrement not null, -- ID
            country   real    default 0 not null,                 -- 年份
            count     integer default 0 not null                  -- 数量
        );
    '''
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.executescript(sql)
    conn.commit()
    cursor.close()
    conn.close()


# 显示图表
def show_rating(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    # 查询数据
    sql = "select * from db_movies_rating order by rating asc"
    rows = cursor.execute(sql)
    # 遍历数据
    x = []
    y = []
    for row in rows:
        x.append(row[1])
        y.append(row[2])

    # 创建一个点数为 8 x 6 的窗口, 并设置分辨率为 80像素/每英寸
    plt.figure(figsize=(10, 10), dpi=80)
    # 包含每个柱子对应值的序列
    values = y
    # 包含每个柱子下标的序列
    index = np.arange(len(x))
    # 柱子的宽度
    width = 0.45
    # 绘制柱状图, 每根柱子的颜色为紫罗兰色
    plt.bar(index, values, width, label="数量")
    # 设置横轴标签
    plt.xlabel('评分')
    # 设置纵轴标签
    plt.ylabel('数量')
    # 添加标题
    plt.title('电影评分数量对比图')
    # 添加纵横轴的刻度
    plt.xticks(index, x)
    # 添加图例
    plt.legend(loc="upper right")
    # 解决中文乱码问题
    plt.rcParams['font.sans-serif'] = ['Simhei']
    plt.show()
    # 关闭数据库连接
    conn.close()


# 显示图表
def show_country(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    # 查询数据
    sql = "select * from db_movies_country order by count desc"
    rows = cursor.execute(sql)
    # 遍历数据
    x = []
    y = []
    for row in rows:
        x.append(row[1])
        y.append(row[2])

    # 创建一个点数为 8 x 6 的窗口, 并设置分辨率为 80像素/每英寸
    plt.figure(figsize=(20, 20), dpi=100)
    # 保证圆形
    plt.axes(aspect=1)
    plt.pie(x=y, labels=x, autopct='%3.1f %%')
    # 添加标题
    plt.title('TOP—250各国占比')
    plt.show()

    # 关闭数据库连接
    conn.close()


# 显示图表
def show_year(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    # 查询数据
    sql = "select * from db_movies_year order by year asc"
    rows = cursor.execute(sql)
    # 遍历数据
    x = []
    y = []
    for row in rows:
        x.append(int(row[1]))
        y.append(row[2])

    # 创建一个点数为 8 x 6 的窗口, 并设置分辨率为 80像素/每英寸
    plt.figure(figsize=(25, 10), dpi=160)
    # 包含每个柱子下标的序列
    index = np.arange(len(x))
    plt.plot(index, y)
    # 添加纵横轴的刻度
    plt.xticks(index, x)
    plt.xlabel("年份")  # 横坐标名字
    plt.ylabel("上映数量")  # 纵坐标名字
    # 添加标题
    plt.title('统计年份上映数量')
    plt.show()

    # 关闭数据库连接
    conn.close()


# 导出到Excel
def export_excel(data):
    # 判空
    if len(data) == 0:
        return
    # 创建Workbook
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet("top250")
    # 表头
    worksheet.write(0, 0, "中文名称")
    worksheet.write(0, 1, "外国名称")
    worksheet.write(0, 2, "上映年份")
    worksheet.write(0, 3, "国家")
    worksheet.write(0, 4, "影片链接")
    worksheet.write(0, 5, "图片地址")
    worksheet.write(0, 6, "影片评分")
    worksheet.write(0, 7, "评价人数")
    worksheet.write(0, 8, "影片概况")
    worksheet.write(0, 9, "相关内容")

    # 遍历设置表内容
    for i in range(1, len(data) + 1):
        item = data[i - 1]
        worksheet.write(i, 0, item['ctitle'])
        worksheet.write(i, 1, item['otitle'])
        worksheet.write(i, 2, item['year'])
        worksheet.write(i, 3, item['country'])
        worksheet.write(i, 4, item['link'])
        worksheet.write(i, 5, item['img'])
        worksheet.write(i, 6, item['rating'])
        worksheet.write(i, 7, item['judge'])
        worksheet.write(i, 8, item['quote'])
        worksheet.write(i, 9, item['info'])

    # 保存文件
    workbook.save("豆瓣TOP_250影片信息.xls")


if __name__ == '__main__':
    baseurl = "https://movie.douban.com/top250?start="
    # 爬取数据
    movies = get_data(baseurl)
    # 保存数据到数据库
    db_path = "douban.sqlite"
    init_db(db_path)
    save_movies(movies, db_path)
    count_movies_rating(movies, db_path)
    count_movies_year(movies, db_path)
    count_movies_country(movies, db_path)
    # 展示图表
    show_rating(db_path)
    show_country(db_path)
    show_year(db_path)
    # 导出电影数据
    export_excel(movies)
