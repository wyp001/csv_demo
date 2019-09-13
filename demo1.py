import csv

'''
    读取csv文件
'''

def read_csv_demo1():
    with open("movies.csv","r",encoding="utf-8") as fp:
        # reader是一个迭代器
        reader = csv.reader(fp)
        # next()函数是将迭代器的指针向下移动一位。此处如果不使用next()函数，读取时将包含第一行（标题行）
        # next(reader)
        for x in reader:
            # 获取第二列ratting数据
            ratting = x[1]
            # 获取最后一列director数据
            director = x[-1]
            print({"ratting":ratting,"director":director})

def read_csv_demo2():
    with open("movies.csv","r",encoding="utf-8") as fp:
        # 使用DictReader()创建的reader对象不会包含标题的那行数据
        # reader是一个迭代器，遍历这个迭代器，返回的是一个字典
        reader = csv.DictReader(fp)
        for x in reader:
            # 获取ratting列数据
            ratting = x["ratting"]
            # 获取director列数据
            director = x["director"]
            print({"ratting": ratting, "director": director})


if __name__ == '__main__':
    # read_csv_demo1()
    read_csv_demo2()
