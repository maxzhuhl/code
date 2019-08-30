# 用循环的方式删除多级目录 （空目录）
# print(os.listdir('a/b/c/d/e'))
# pathStr = 'a'
# while(1):
#     pathStr = pathStr+'/'+os.listdir(pathStr)[0]
#     if(os.listdir(pathStr)):
#         pass
#     else:
#         break #a/b/c/d/e
# # print(pathStr.count('/'))
# for i in range(pathStr.count('/')+1):
#     os.rmdir(pathStr)
#     pathStr = pathStr[:-2]
#重命名、删除文件
import os
filepath = os.getcwd()+'/'
#os.rename(filepath+'file.txt',filepath+'filea.txt')#重命名
#os.remove(filepath+'filea.txt')#删除文件

#目录操作
# os.mkdir(filepath+'untitled2')
# os.chdir(filepath+'untitled2')#绝对文件
# os.chdir('untitled2')#相对路径
# print(os.getcwd())
# os.chdir('..')#支持..返回上一层操作
# print(os.getcwd())
# os.rmdir(filepath+'T109')#删除目录
# os.makedirs(filepath+'T109/1/2/3/4/5/6')#创建多级目录
print(os.path.isdir(filepath+'T109'))#判断是否是文件夹
print(os.path.isfile(filepath+'demo1.py'))#判断是否是文件
#if os.path.isdir(filepath+'T109'):
# import shutil
# shutil.rmtree(filepath+'T109')#删除多级目录
# os.mkdir('T109')
# os.chdir('./T109')
# for i in range(1,101):
#     #os.mkdir('K_%03d'%i)
#     file=open('K_%03d.txt'%i,'w')
#     file.write('T109')
#     file.flush()
#     file.close()

#日期时间time模块
# import time #python中，时间是一个元组
#
# now = time.time()
# print(now)#获取当前时间
# nowtuple=time.localtime( now )
# print(nowtuple)
# for i in range( len(nowtuple) ):
#     print(nowtuple[i])
# #年月日时分秒一周的第几天 一年的第几天 夏令时
#
# strtime = time.strftime("%Y-%m-%d %H:%M:%S %p",nowtuple)
# print(strtime)
# #英文时间显示
# engtime = time.asctime(nowtuple)
# print(engtime)
# #给定时间元组转换成时间戳
# timeup = (2019,8,22,15,28,9,2,250,0)
# time1 = time.mktime(timeup)
# print(time1)
#获取当前时间
# import datetime
# now = datetime.datetime.today()
# print(now)
# now = datetime.datetime.now()
# print(now)
# #把当前时间转换成时间戳
# n = now.timestamp()
# print(n)
# #把当前时间转换成时间元组
# ntu = now.timetuple()
# print(ntu)
# #自定义日期格式显示时间
# st = now.strftime('%Y-%m-%d')
# print(st)
# #通过时间元组截取部分的日期字符串(比如年月日时分秒)
# print(ntu.tm_mon)
# a = datetime.datetime(2019,8,26,16,15,45)#自定义一个DATETIME类型进行操作
# print(a.timestamp())

# import os
# a = os.getcwd()+'test.txt'
# b = open(a,'r',encoding='UTF-8')
# c = b.readlines()
# print(c)
# listz = [-1,-10,2,8,63,-8]
# listz.sort()
# listz.reverse()
# # len(listz)
# print(listz)
# print (len(listz))

sum = 0
n = 20
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)