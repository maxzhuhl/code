# # #列表
# # lista = [1,2,3,'hello',10.5,5,6]
# # listb = [1,2,3]
# #lista[2] = 5 #把2赋值为5
# # print(lista[3])
# # print(lista)
# # print(lista[1:4])
# # print(lista[3:-1])
# # print(lista[3:])
# # print(lista[:4])
# # print(lista*2)
# # print(lista+listb)
# #
# # #列表中的方法
listc = []
listc.append(1)
listc.append(2)
listc.append(3)
listc.append(4)
listc.append(5)
listc.insert(3,6)
print(listc)
# listc = [1,2,3,4,5]
# listc.append(3)#添加一个元素
# listc.insert(3,6)
# #listd = [4]
# print(listc)
# #print (type(a)) #显示类型
# # listc.insert(1,5)#在指定位置添加一个元素
# # print(listc)
# # a=listc.pop(3)#删除指定位置的元素并返回该元素的值
# # print(a)
# # print(listc)
# # listc.remove(1) #删除第一次出现的元素
# # print(listc)
# # print(listc.count(1))#统计元素在列表中出现的次数
# # print(list.index(1))#显示元素在列表中的下标
# # listc.extend(listd)#listc=listc+listd 追加列表
# # print(listc)
#
liste = [8,4,10,33,75,-8,98,15]
liste.sort()#排序
print(liste)
liste.reverse()#反转
print(liste)

listz = [3,6,9,4,10]
listz.sort()
listz.reverse()
len(listz)
print(listz)
print (len(listz))

tup1=tuple(listz)
print(tup1)
print(set(listz))

# listm = [4,5,4,3,9,0,3]
# print(set(listm))
listm = [1,2,3,int(40.5),6]
print(listm)