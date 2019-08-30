# class people():
#     def __init__(self,n,s,a):
#         self.name = n
#         self.sex = s
#         self.age = a
# #可以把类当成一个数据类型来看
# lista = [1,2,'hello']
# lista = [1,3,'hello']
# print(lista[1])
# peoplea=people('aaa','男',33)
# peoplea=people('bbb','男',33)
# print( isinstance(peoplea.people))
# print( isinstance(lista,list))
#
#
#
# #抽象类写法（）语法
# import abc
# class a1(metaclass=abc.ABCMeta):
#     @abc.abstractmethod
#     def aa(self,a,b,c):
#         pass
# from abc import ABCMeta,abstractmethod
# class a2(metaclass= ABCMeta):
#     @abstractmethod
#     def aa(self,a,b,c):
#         pass
#
# class a3(a2):
#     def aa(self,a,b,c):
#         print(a)
# aaaa=a3()
# class a4(a2,metaclass=ABCMeta):
#     pass

# from abc import ABCMeta,abstractmethod
# class friut(metaclass=ABCMeta):
#     def __init__(self,n,p):
#         self.name=n
#         self.price=p
#     @abstractmethod
#     def eat(self,t):
#         pass
#
# class apple(friut):
#     def __init__(self,n,p):
#         friut.__init__(self,n,p)
#     def eat(self,t):
#         print(self.name+'用水果刀' + str(t) + '后吃')
#
# class orange(friut):
#     def __init__(self,n,p):
#         super().__init__(n,p)
#     def eat(self,t):
#         print('用手' + str(t) + '后吃')
# a=apple('红富士',18)
# o=orange('丑橘',3)
# a.eat('削皮')
#
# class file(metaclass=ABCMeta):
#     @abstractmethod
#     def doubleClick(self):
#         pass
# class txtfile(file):
#     def doubleClick(self):
#         print('查看txt文件内容')
# class exefile(file):
#     def doubleClick(self):
#         print('执行exe文件')
# class imgfile(file):
#     def doubleClick(self):
#         print('浏览图片')
# def openFile(fileObject):
#     fileObject.doubleClick()
#
# txtf=txtfile()
# openFile(txtf)
# exef=exefile()
# openFile(exef)
#
# #异常
# try:
#     a='hello'+10
# except TypeError as e:
#     print(e)
#     print('类型出错')
# print('hello,world')
#
# indexnum = int(input('请输入页码'))
# books=[1,2,3,4,5,6]
# try:
#     print(books[indexnum])
# except IndexError as e:
#     print('页码输入过大，显示首页数据：'+str(books[0]))
#
#
# try:
#     a='hello'+10
#     books=[1,2,3,4,5,6]
#     print(books[6])
# except TypeError as e:
#     print('系统报错，原因不明')
# except IndexError as e:
#     print('页码输入过大')
# except TypeError as e:
#     print('类型出错')
#
# #finally语句使用
# indexnum = int( input('请输入页码'))

from selenium import webdriver
import os
chromePath='C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python37\\chromedriver.exe'
# print(os.getcwd())
os.environ['webdriver.chrome.driver']=chromePath
driver = webdriver.Chrome(executable_path=chromePath)
driver.get('https://www.baidu.com')

