import csv
'''
    将csv数据写入文件
'''


# 使用元组的形式将数据写入到csv文件中
def wriite_csv_demo1():
    # 定义标题行
    headers = ["username", "age", "hight"]
    # 要写入的数据（元组的形式）
    values = [
        ("张三", 18, 180),
        ("李四", 19, 175),
        ("王五", 20, 170)
    ]
    # newline参数不指定的话，默认为\n，即会在新建的每一行后面对一个换行符。
    # 如果不想要每写入一行数据就添加一个空行的话，可将newline参数设置为空字符串
    with open("students.csv","w",encoding="utf-8",newline="") as fp:
        writer = csv.writer(fp)
        writer.writerow(headers)
        writer.writerows(values)

# 使用字典的形式将数据写入到csv文件中
def wriite_csv_demo2():
    headers = ["username", "age", "hight"]
    values = [
        {"username":"张三","age":10,"hight":170},
        {"username":"李四","age":20,"hight":180},
        {"username":"王五","age":30,"hight":190},
    ]
    with open("students02.csv","w",encoding="utf-8",newline="") as fp:
        writer = csv.DictWriter(fp,headers)
        # 写入表头数据时，需要调用writerheader()方法
        writer.writeheader()
        writer.writerows(values)

if __name__ == '__main__':
    wriite_csv_demo2()