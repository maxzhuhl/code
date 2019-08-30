#函数基础
# def pria():
#     print('hello,world')
#     print('nihao')
# pria()

#形参，实参
# def prib(str):   #str形参
#     print('您输入的是:'+str)
#     prib('hello')   #hello 实参

#函数的返回值
# def add(num1,num2):
#     num3=num1+num2
#     return  num3
# suma = add(3,4)
# print(suma)

#函数参数传递
#列表参数传递举例
# def addlist(s):
#     s.append(10)

# k = [1,2,3,4,5]
# print(k)
# addlist(k)
# print(k)

#数字，字符串，元组
# def addlist(s):
#     print(id(s))
#     s.append(10)
#
# g = (1,2,3,4,5)
# print(id(g))
# print(g)
# addlist(g)
# print(g)

#字典的例子
# def edict(s):
#     a=[]
#
# g = {1,2,3,4}
# print(id(g))
# print(g)
# edict(g)
# print(g)

#必备参数
# def adda(a,b,c):
#     return a+b+c
# print(adda(10,20,30)) #实参必须传递三个，不然会报错

#关键字参数
# def addb(a,b,c):
#     print('a:' + str(a),end=',')
#     print('b:' + str(b), end=',')
#     print('c:' + str(c), end=',')
# addb(1,2,3)
# addb(c=5,a=6,b=8) #关键字参数体现在实际参数上，根据形参的变量名进行传递

#默认参数1
# def addc(a,b=10,c=20):  #给b，c默认值
#     return a+b+c
# print(addc(20))
# print(addc(20,60))
# print(addc(20,60))
# print(addc(50,c=30)) #print（addc(c=30,50))不行，因为50是b位，而a还是没有值

#默认参数2
# def addc(a,c,b=10): #给b，c默认值 默认值有1个必须放在最后面，有多个也要放在后面
#     return  a+b+c
# print(addc(20))
# print(addc(20,60))
# print(addc(50,c=30))#print（addc（c=30,50）不行，因为50是b位，而a还是没有值

#函数参数类型下
#收集参数，不定长参数，两种类型
#收集参数
# def pria(*ppp):
#     for p in ppp:
#         print(p)
# pria()
# pria(10)
# pria(10,20)
# pria(10,20,30,40,50)

#收集参数2 **
# def prib(**kkk):
#     print(type(kkk))
#     for k in kkk:
#         print(str(k)+':'+str(kkk[k]),end=' ')
# prib()
# prib(a=10)
# prib(a=10,b=20)

#函数的嵌套
# def adda(x):
#     print('调用函数adda')
#     addb(x)
# def addb(y):
#     print('调用函数addb')
#     print(y+20)
# adda(20)
# addb(30)

# #嵌套定义
# def addc():
#     pass  #空语句，表示啥都不做
#     def addd():
#         pass
#有真实的作用，内部的函数如何调用
# def adde(s):
#     c = s +10
#     print('调用函数adde')
#     def addf(d): #嵌套定义的函数一般只在外层中调用
#         print('请调用函数addf')
#         e = d + 30
#         return e
#     f = addf(c) #嵌套定义函数的调用
#     print('结果'+str(f))
#     adde(50)

#变量的作用域 LEGB法则
# print(__name__)
#局部作用域
# def a(p):
#     c=p+10 #局部作用域
#     print(c)
# a(20)
# print(c) #c不能在外层执行，因为是局部作用域
# def b(p):
#     k = p +10#相对于函数c来讲是嵌套作用，相对于函数b来说是局部作用域
#     print(k)
#     def c():
#         y=5 #局部作用域
#         print(y)
#     c()
#全局作用域
# u = 20
# def d():
#     #u=40
#     print(u)
# d()
# print(u)

#如何在函数内使用全局变量
# u = 20
# def d():
#     global u  #表示全局变量u，函数内就不再定义新局部变量
#     u=40
#     print(u)
# d()
# print(u)

#内置所有变量
# s = vars()
# print(s)
# for di in list(s.keys()):
#     print(str(di)+':'+str( s[di] ))

# #变量的作用域LEGB法则，下
# print(__file__)#B
# __file__ = 20
# def a():
#     __file__ = 30#E
#     print(__file__)
#     def b():
#         __file__ = 40#L
#         print(__file__)
#     b()
# a()

#匿名函数
adds = lambda num1,num2:num1+num2

def addk(num1,num2):
    return num1+num2
print(adds(1,2))
print(addk(1,2))

#函数递归
#举例1：
# def a():
#     print('hello')
#     a()
# a()
#举例2:间接递归
# def b():
#     print('hello')
#     c()
# def c():
#     print('hello')
#     b()
# b()

#例子3：
# def num(n):
#     if n ==1:
#         return  1
#     return  num(n - 1) +2
# print(num(5))

#例子4
def num(n):
    if n <= 1:
        return  1
    return  num(n - 1) +num(n - 2) +2
print(num(5))