```
#coding:utf-8


import xml.dom.minidom
import os


def getxml(value=None):
    '''获取单节点的数据内容'''
    xmlFile=xml.dom.minidom.parse('data1.xml')
    db=xmlFile.documentElement
    itemList=db.getElementsByTagName(value)
    item=itemList[0]
    return item.firstChild.data
```
```
print(getxml('admin'))

函数中用到parent参数，但不确定传递什么参数，给它默认一个参数值None
def getUser(parent=None,child=None):
    '''获取单节点的数据内容'''
    xmlFile=xml.dom.minidom.parse('data1.xml')
    db=xmlFile.documentElement
    itemList=db.getElementsByTagName(parent)
    item=itemList[0]
    return item.getAttribute(child)
 # 父节点：WuYa 子节点：nick
print(getUser('WuYa','nick'))
```
```
def getUser(parent='WuYa',child=None):
    '''获取单节点的数据内容'''
    xmlFile=xml.dom.minidom.parse('data1.xml')
    db=xmlFile.documentElement
    itemList=db.getElementsByTagName(parent)
    item=itemList[0]
    return item.getAttribute(child)
print(getUser(child='address'))

```
