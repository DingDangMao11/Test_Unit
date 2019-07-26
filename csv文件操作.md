##  在项目根目录下创建csv文件（以另存为的方式）
```
#coding:utf-8

import  csv

def readCsvList():
    with open('csv.csv','r') as f:
        reader = csv.reader(f)
        # 不读标题行
        next(reader)
        db=[item for item in reader]
        print(db)

readCsvList()
# 查看列表类型
print(type(readCsvList()))
输出结果
<class 'NoneType'>
--------------------------------------------------------------------------------
def readCsvList():
    with open('csv.csv','r') as f:
        reader = csv.reader(f)
        # 不读标题行
        next(reader)
        for item in reader:
            print(item)

```
