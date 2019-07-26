#coding:utf-8

import  csv

def readCsvList():
    with open('csv.csv','r') as f:
        reader = csv.reader(f)
        # 不读标题行
        next(reader)
        for item in reader:
            print(item)

readCsvList()

