#1+..+10
# def add(n):
#     if n==1:
#         return  1
#     return add(n-1)+n
# print(add(10))

#内置模块
# print(help('modules')) #查看所有内置模块
#sys,os
# import sys,os
# print(sys.platform)
#自定义模块调用 否
#print(add(3,4))

#2.用模块名函数名能否调用  否
#print(demo_02,add(3,4))
#先使用impo导入再调用
# import demo_02  #导入模块
# #print(demo_02.add(3,4))
#
# from demo_02 import  add #使用from import导入函数
# print(add(3,4))
#
# from demo_02 import * #导入所有的函数，（不建议使用）
# print(mul(3,4))
#
# from demo_02 import  add as d #给函数取别名
# print(d(3,4))
# def peven(n):
#     s = 0.0
#     for i in range(2,n + 1,2):
#         s += 1.0 /i
#         print('值：',s)
# def podd(n):
#     s=0.0
#     for i in range(1,n + 1,2):
#         s += 1.0/i
#         print('值:',s)
# n=int(input('输入一个数：'))
#
# if n % 2 ==0:
#     peven(n)
# else:
#     podd(n)

# i = 0
# for x in range(1,5):
#     for y in range(1,5):
#         for z in range(1,5):
#             if (x!=y) and (y!=z) and (z!=x):
#                 i += 1
#                 if i%4:
#                     print("%d%d%d" % (x,y,z),end="|")
#                 else:
#                     print("%d%d%d" % (x,y,z))

# s = 0
# def mul(n):
#     if n==1:
#         return 1
#     return n*mul(n-1)
# for n in range(1,21):
#     a=mul(n)
#     s += a
# print(s)
def func():
    print('this is my own sys.py')
func(c)