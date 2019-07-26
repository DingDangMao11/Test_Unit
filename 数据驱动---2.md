## 同一项目目录下，创建初始文件config.ini

### config.ini
```
[linux]
IP=191.168.1.1
PORT=22
USERNAME=root
PASSWORD=kaflafjkgsl
```
### data.py 
```
#coding:utf-8

import configparser
import os

def base_dir(filename=None):
    return os.path.join(os.path.dirname(__file__),filename)
def getlinux():
    list1=[]
    config=configparser.ConfigParser()
    config.read(base_dir('config.ini'))
    ip=config.get('linux','IP')
    port = config.get('linux', 'PORT')
    username = config.get('linux', 'USERNAME')
    pasword = config.get('linux', 'PASSWORD')
    list1.append(ip)
    list1.append(port)
    list1.append(username)
    list1.append(pasword)
    return list1
    
--------------------------------------------------------------------------------------------------------------
def getlinux(Linux='linux'):
    list1=[]
    config=configparser.ConfigParser()
    config.read(base_dir('config.ini'))
    ip=config.get(Linux,'IP')
    port = config.get(Linux, 'PORT')
    username = config.get(Linux, 'USERNAME')
    pasword = config.get(Linux, 'PASSWORD')
    list1.append(ip)
    list1.append(port)
    list1.append(username)
    list1.append(pasword)
    return list1

print(getlinux()[0])
```
