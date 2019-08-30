#字典 (dict) 无序 {} key:value
dicta ={}
dictb = {'n1':8,'n2':'hello'}
print(dicta)

dictc = dict()
dictd = dict(n1=8,ne='hello')

lista = ['A1','A2','A3']
dicte = dict.fromkeys(lista,'hehe')

dict = {}.fromkeys(('x','y','z'),6)
print(dict)

#字典的增删改查
dictg = {'n1':8,'a2':'hello'}
dictg['n3']='kkk' #项不同的时候进行新增
print(dictg)
dictg['n2']=66#项相同的时候进行修改
print(dictg)
del dictg['n3'] #删除
print(dictg)

#字典的方法
dicth = {'A1':8,'A2':7,'A3':8}
print(dicth.keys())#返回字典所有的key
print(dicth.values())#返回字典所有的value
print(dicth.get('A2'))#返回指定key的value
s = dicth.pop('A2')#获取并删除指定key的项
print(s)
print(dicth)
dicth.update(A3=12)#添加或修改键值对
print(dicth)
# dicth.clear()#清楚整个字典
# print(dicth)

