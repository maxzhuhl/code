# #序列操作总结
# #len() + * max() main() in
# a = '123456'
# b = [1,2,3,4,5,6]
# c = (7,8,9,10,11,12)
# d = {1,2,3,4,5}
# e = {'A1':1,'A2':2}
#
# print(len(a),len(b),len(c),len(d),len(e))
# a1 = a +'123' ; print(a1)
# b1 = b+[1,2,3];print(b1)
# c1 = c+(7,8,9);print(c1)
# a2 = a*2;print(a2)
# print(max(a),max(b),max(c),max(d),max(e))
# print('3' in a);print(5 in d);print('A1' in e)
#
# lista = ['23.34%','30.88%','6.99%']
# lista[0] = float[0]

#输入输出语句
#

# #运算符
# a = 5//3
# print(a)
# a= 5%3
# print(a)
# a = 5++3
# print(a)
#
# a=3
# a+=5;print(a) #a=a+5
# a%=2;print(a)
# #关系运算符
# print(5!=5)
# #逻辑运算符
# print(3>5 or 5>6)
# print(not 3>5)
# #位运算符(先求出每个数的二进制，按位算)
# print(10 & 6)
# print(~10)
# #三元运算符
# s = 10 if 10>5 else 5 #10>5?10:5
# print(s)
# #输入两个数，求出最大值，max()三元
# s1=int(input('请输入s1:'))
# s2=int(input('请输入s2:'))
# print(s1 if s1>s2 else s2)
# print(max(s1,s2))
#成员运算符in not in 返回结果是布尔类型
# print(3 in[3,5])
#身份运算符 is is not id()求变量的地址的，身份相同表示变量地址相同
# i = 1
# print( id(1) )
# print( id(1) )
# print(i is 1)
#
# j = 1
# print( id(1) )
# print( id(j) )
# print(j is 1)
#
# k=[1,2,3]
# p=[1,2,3]
# print(id([1,2,3]))
# print(id(k))
# print(id(p))
#多行语句
# a =\
# 30
# print(a)
#真值条件，任何非0和飞空
# a = 10>5 #1 'A' [1,2] true
# if a:
#     print('为真！！！')
#
# num1 = int(input('请输入num1:'))
# num2 = int(input('请输入num2:'))
# if num1>num2:
#     print('num1>num2')
# elif num1==num2:
#     print('num1=num2')
# else:
#     print('num1<num2')

#输入A  显示优秀 输入B 显示良好 输入C显示一般 输入D显示差 输入其他显示报错
# E = input('请输入等级：')
# if E=='A':
#     print('优秀')
# elif E=='B':
#     print('良好')
# elif E=='C':
#     print('一般')
# elif E=='D':
#     print('差')
# else:
#     print('输入有错')

#while语句
# sum = 0
# i = 1
# while(i<=10):
#     sum+=i
#     if(i==10):
#         break
#     i=i+1
# else:
#         print(sum)
#
# sum = 0
# i = 1
# while(i<=10):
#     i = i + 1
#     if(i%2==1):
#         continue
#     sum += i
# else:
#         print(sum)

#range()函数
# a = range(10)
# print(list(a))
#
# a = range(1,10)
# print(list(a))
#
# a = range(1,10,2)
# print(list(a))

#for 循环
# for c in 'letter':
#     print(c,end=',') #end 表示以什么符号结束，默认换行
#
# lista = [20,30,50,80]
# print()
# for k in lista:
#     print(k,end=' ')
#
# for p in range(1,11):
#     print(p,end=' ')