##  在项目根目录下创建csv文件（以另存为的方式）
### 列表
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

```
def readCsvList():
    with open('csv.csv','r') as f:
        reader = csv.reader(f)
        # 不读标题行
        next(reader)
        for item in reader:
            #列表的强制类型转换
            #print(list(item))
            print(list(item)[0])
            输出结果：
            LOGIN__001
            LOGIN__002
            LOGIN__003
            LOGIN__004
            print(list(item)[1])
            输出结果：
            http://www.baidu.com
            http://www.baidu.com
```
###  字典

```
def readCsvDict():
    with open('csv.csv','r') as f:
        reader = csv.DictReader(f)
        for item in reader:
            print(dict(item))
            
 输出结果：
{'caseID': 'LOGIN__002', 'URL': 'http://www.baidu.com'}
{'caseID': 'LOGIN__003', 'URL': 'http://www.baidu.com'}
{'caseID': 'LOGIN__004', 'URL': 'http://www.baidu.com'}

```
```
def readCsvDict():
    with open('csv.csv','r') as f:
        reader = csv.DictReader(f)
        for item in reader:
            print(dict(item)['caseID'])
readCsvDict()

输出结果：
LOGIN__001
LOGIN__002
LOGIN__003
LOGIN__004
```
