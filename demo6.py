#数据类型转换
#自动转换
a = 10+20.5 #==> 10.0+20.5
print(a)
b = [3,2]+[6,6]
print(b)

b = str(10)+'2'
print(b)
c = 10+int('2')
print(c)

d = chr(48)#把整数换成ASCII码的字符
print(d)

e = ord('A')
print(e)

com = 'print("ccc")'
eval(com)
repr(com)
