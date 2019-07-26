#coding:utf-8

import configparser
import os

def base_dir(filename=None):
    return os.path.join(os.path.dirname(__file__),filename)
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



