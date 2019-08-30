#面向对象基础语法学习
# class peopleB():
#     className = '人类' #类对象的属性
#     classAttribCount = 3 #类对象的属性
#     def __init__(self,n,a): #__init__初始化方法，构造方法
#         self.peopleName = n #实例属性 对象属性
#         self.peopleAge = a #实例属性 对象属性
# #self 类型java中的this 代表对象（实例本身） 默认使用self随便用什么都可以
# #创建对象语法 对象名+类名(属性值列表)
# xiaoming = peopleB('小明',32)#self不需传组 但是必带
# print(xiaoming.peopleName,xiaoming.peopleAge)

#私有属性，内置属性
# class peopleB():
#     className = '人类'
#     classAttribCount = 3
#     def __init__(self, n, a,m):
#         self.peopleName = n
#         self.peopleAge = a
#         self.__money = m#私有属性
#     def priMoney(self):
#         print(self.__money)
# xiaoming = peopleB('小明',22,3000)
# print(xiaoming.peopleName)
# print(xiaoming.peopleAge)
# # print(xiaoming.__money)
# xiaoming.priMoney()
#
# #内置属性
# print(peopleB.__dict__)#显示类的属性字典
# print(peopleB.__doc__)#打印类的文档信息
# print(peopleB.__name__)#类的名称
# print(peopleB.__module__);print(__name__)#功能一致，但写法不一致
# print(peopleB.__bases__)#显示当前类的父类信息

#构造方法，实例方法（私有）、类方法、静态方法、内置方法
# class peopleB():
#     def __init__(self, n, a):
#         self.peopleName = n
#         self.peopleAge = a
#     def study(self,c): #实例方法ollllloo
#         print(self.peopleName+'学习'+c)
#     def __getmoney(self,n): #私有方法实例
#         print(self.peopleName+'通过私有方法取钱：'+str(n))
#     @classmethod #修饰器 表明下面的方式是类方法
#     def priPeopleClassInfo(cls,a):#cls代表类本身，可以换其他标志符，但必须有
#         print('获取人类的基本属性信息'+str(a))
#     @staticmethod
#     def inout(n):
#         print('输入的是：'+str(n))
#
# xiaoming = peopleB('小明',22)
# xiaoming.study('语文')
# peopleB.priPeopleClassInfo('age')#类方法的访问 类名，方法名，cls不用传参数
# peopleB.inout('xiao')

# #类方法
# class pepoleB():
#     name = '人类'
#     @classmethod #修饰器
#     def setClassName(cls,n):#修改类属性
#         cls.name = n
#内置方法
class peopleB():
    classname = '人类'
    def __init__(self,n,s):
        print('我是初始化init方法')
        self.peoplename = n
        self.score = s
    def __del__(self):
        print('我是析构释放del方法')
        del self.peoplename
    def __str__(self):
        return 'hello'
    def __add__(self, other):
        return self.score + other.score
xiaoming = peopleB('小明',60)
print(xiaoming.peoplename)
print(xiaoming.__str__())
print(xiaoming.__getattribute__('peoplename'))
xiaohei = peopleB('小黑',80)
print(xiaoming + xiaohei)

