# print('hello python')
# #数据类型
# import sys
# i = 30000
# print(type(i))
# print(sys.getsizeof(i))
#
# j = 10.5
# print(type(j))
#
# o = 3.2e3
# print(o)
#
# k = True
# print(k+1)
#
# #字符串切片
x='12345678'
print(x[2:0])
print(x[2:-1])
# print(x[-4:-1])
# print(x[-4:])
#
# #字符串操作符
# print(a+b)
# print(a*3)
#
#字符串函数
# print(a.capitalize())
# print('HELlo'.upper())
# print('HELlo'.lower())
# print('hello'.replace('he','oopp'))
# print('China,USA,English'.split(','))
# print(a.islower())
# print(len(a))

# #字符串格式化
# str = '%s,hello'
# print(str%'lipu' )
# print('hello,%s'%'lipu')
# print('%d+%d=%d'%(1,2,1+2))
# print('123%+dppp'%4)   #%+d +显示正负号
# print('123%+5dppp'%-4) #%+5d 5表示最小宽度 不足以空格去补
# print('123%05dppp'%48888)
#
# str = '3'
# print('3%06dppp'%20)

# print('123%4.2fppp'%20.1234)#带小数点位数的显示
# print('123%7.2fppp'%20.1234)
#
# print('%o'%8)#无符号8进制
# print('%x'%22)#无符号16进制

# 斐波那契数列 输入一个数字，求出数字代表的斐波那契数列的数据，
# 	 斐波那契数列（Fibonacci sequence），又称黄金分割数列，
# 	 指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
# inputnum = int (input('输入一个数字：\n'))
# i=2
# lista=[0]
# if inputnum>=1:
#     lista.append(1)
# while(1):
#     c=lista[i-2]+ lista[i-1]
#     if (c<=inputnum):
#         lista.append(c)
#     else:
#         break
#     i=i+1
# print(lista)
# x="foo"
# y=2
# print(x+y)
