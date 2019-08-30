#算法代码
#交换算法
# a = 10; b=20
# a,b = b,a
# print(a,b)

#2.求输入数据中的最大值，值为N N=3
# a = 80 ; b =10;c=95
# max = a;
# if(max<b):
#     max = b
# if(max<c):
#     max=c
# print(max)
#方法2
# m = 0
# for i in range(3):
#     inputnum=int(input('输入第'+str(i+1)+'个值'))
#     m = max(m,inputnum)
# else:
#     print(m)

#方法3
# m = 0
# for i in range(3):
#     inputnum=int(input('输入第'+str(i+1)+'个值'))
#     if m <inputnum:
#         m=inputnum
# else:
#     print(m)

#方法4:把输入的数据保留到列表中，最后使用max函数
# numlist = []
# for i in range(3):
#    inputnum=int(input('输入第'+str(i+1)+'个值'))
#    numlist.append(inputnum)
# else:
#    print(numlist)

#方法5：把输入的数据保留到列表中，先排序然后输出
# numlist = []
# for i in range(3):
#    inputnum=int(input('输入第'+str(i+1)+'个值'))
#    numlist.append(inputnum)
# else:
#    print(numlist.sort()[-1])

#3.求2--100中的质数，除了1和他本身以外不在有其他因数
#判断是否是质数
# num = int(input('请输入'))
# for i in range(2,num):
#     if num%i==0:
#         print(str(num)+'不是质数')
#         break
# else:
#     print(str(num)+'是质数')

# for j in range(2,101):
#     for i in range(2,j):
#         if j%i==0:
#         # print(str(num)+'不是质数')
#             break
#     else:
#      print(str(j),end=',')

#打印九九乘法表
# for i in range(1,10):
#      for j in range(1,i+1):
#          print('%d*%d=%2d' % (i,j,i*j),end=' ')
#      print (' ')
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('{}x{}={}\t'.format(j, i, i*j), end='')
#     print()

# print('1*1=1')
# print(str(1)+'*'+str(1)+'='+str(1*1))
# print('%d*%d=%d'%(1,1,1*1))
# print('{}*{}={}'.format())

#升序排序
#方法一
# lista = [80,-2,66,90,33]
# lista.sort()
# print(lista)
#方法二min函数 pop取并且删
# listb = []
# for i in range(len(lista)):
#  listb.append(lista.pop(lista.index(min(lista))))
# print(listb)
#方法三：冒泡排序
# listc = [80,-2,66,90,33,7]
# for i in range(5):
#       if(listc[i]>listc[i+1]):
#         listc[i],listc[i+1] = listc[i+1],listc[i]
# print(listc)
# for i in range(4):
#  if(listc[i]>listc[i+1]):
#         listc[i],listc[i+1] = listc[i+1],listc[i]
# print(listc)
# for i in range(3):
#  if(listc[i]>listc[i+1]):
#         listc[i],listc[i+1] = listc[i+1],listc[i]
# print(listc)
# for i in range(2):
#  if(listc[i]>listc[i+1]):
#         listc[i],listc[i+1] = listc[i+1],listc[i]
# print(listc)
# for i in range(1):
#  if(listc[i]>listc[i+1]):
#         listc[i],listc[i+1] = listc[i+1],listc[i]
# print(listc)
# for j in range(5,0,-1):
#     for i in range(j):
#      if(listc[i]>listc[i+1]):
#             listc[i],listc[i+1]=listc[i+1],listc[i]
# print(listc)

#二分法排序
# listd = [80,-2,66,33,90,38]
#1.把最小的数和第一个数交换
# print(min(listd))
# # print(listd.index(min(listd)))
# # listd[0],listd[1] = listd[1],listd[0]
# # print(listd)

# ids = listd.index(min(listd[0:]))
# listd[0],listd[ids] = listd[ids],listd[0]
# print(listd)
#
# ids = listd.index(min(listd[1:]))
# listd[1],listd[ids] = listd[ids],listd[1]
# print(listd)

# i=0
# while i<=4:
#     ids = listd.index(min(listd[i:]))
#     listd[1], listd[ids] = listd[ids], listd[i]
#     print(listd)
#     i=i+1
# print(listd)

# 每次把最大的下标和有序的第一个交换 【有序区】【无序区】 选择排序
# lista = [99,68,-10,27,44,90,62,-55,41,0]
# for i in range(9):
#     max_id = i
#     for j in range(i+1, len(lista)):
#         if (lista[max_id] < lista[j]):
#             max_id = j
#     lista[i], lista[max_id] = lista[max_id], lista[i]
# print(lista)
# max_id = 0
# for i in range(1,len(lista)):
#     if(lista[max_id]<lista[i]):
#         max_id = i
# lista[0],lista[max_id] = lista[max_id],lista[0]
#
# max_id = 1
# for i in range(2,len(lista)):
#     if(lista[max_id]<lista[i]):
#         max_id = i
# lista[1],lista[max_id] = lista[max_id],lista[1]
#
# max_id = 2
# for i in range(3,len(lista)):
#     if(lista[max_id]<lista[i]):
#         max_id = i
# lista[2],lista[max_id] = lista[max_id],lista[2]

# mpStr = input('请输入字符串：')
# alphaNum=0
# numbers=0
# spaceNum=0
# otherNum=0
# for i in mpStr:
#     if i.isalpha():
#         alphaNum +=1
#     elif i.isnumeric():
#         numbers +=1
#     elif i.isspace():
#         spaceNum +=1
#     else:
#         otherNum +=1
# print('字母=%d'%alphaNum)
# print('数字=%d'%numbers)
# print('空格=%d'%spaceNum)
# print('其他=%d'%otherNum)
#
# fibs = [0,1]
# for i in range(8):
#  fibs.append(fibs[-2]-fibs[-1])
# print(fibs)

# for i in range(100,1000):
#    if i==sum(int(c)**3 for c in str(i)):
#        print(i)