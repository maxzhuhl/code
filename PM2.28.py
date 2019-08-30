#封装 数据封装、方法封装
# class people():
#     def __init__(self,n,m):
#         self.__name = n
#         self.__name = m
# #创建类和对象时，分别创建两者的名称空间，只能通过类名加"."或者obj的方式访问里面的名字
# xiaoming = people('小红',0000)
# print(xiaoming.__people__name)

# class peopleB():
#     def __init__(self,n,m):
#         self.__name = n
#         self.__money = m
#     def getName(self):#方法封装
#         return self.__name
#     def setName(self,n):
#         self.__name = n
# xiaohong = peopleB('小红',000)
# print(xiaohong.getName())
# xiaohong.setName('小红花')
# print(xiaohong.getName())
#
# #封装 数据封装、方法封装
# class people():
#     name = '人类'
#     def __init__(self,n,a):
#         self.__name = n
#         self.__age = a
#     def eat(self,food):
#         print(self.__name + '吃' + str(food))
# class student():
#     name = '学生类'
#     def __init__(self,n,a,c):
#         self.__name = n
#         self.__age = a
#         self.__class = c
#     def eat(self,food):
#         print(self.__name+'吃'+str(food))
#     def study(self,course):
#         print(self.__name+'学'+str(course))
#
# #继承的语法
# class animal():
#     def eat(self,food):
#         print('吃'+str(food))
# class tiger(animal):
#     pass
# t=tiger()
# t.eat('肉')
#
# #继承的语法
# class animalA():
#     def __init__(self,t,a,w):
#         print('animalA1')
#         self.animalType = t
#         self.animalAge = a
#         self.weight = w
#     def eat(self,food):
#         print('吃'+str(food))
#
# class tiger(animalA):
#     def __init__(self,a,w,c):
#         print('tiger1')
#         animalA.__init__(self,'肉食动物',a,w)
#         print('tiger2')
#         self.category = c
#     def run(self,adderss):
#         print(self.category+'跑向' + str(adderss))
# t1=tiger(6,100,'东北虎')
# print(t1.category,t1.animalType,t1.animalAge,t1.weight)
# t1.eat('肉')
# t1.run('树林')
#
# class tiger(animalA):
#     def __init__(self,a,w,c):
#     #def eat(self,food):
#        # print('吃'+str(food))
# #class tiger(animal):
#     def eeat(self):
#         animal.eat(self,'肉')
#     def eeat1(self):
#         super().eat('肉')
#     def eeat2(self):
#         super(tiger,self).eat('肉')
# t1=tiger(6,100,'东北虎')
# print(t1.category.t1.animalType,t1.animalAge,t1.weight)
# t1.eat('肉')

# class Animal():
#     def __init__(self,a,b,c,d):
#         self.name=a
#         self.type=b
#         self.age=c
#         self.sex=d
#     def eat(self,foot):
#         print(self.name+'吃'+str(foot))
# class Dog(Animal):
#     def __init__(self,a,b,c,d,w,sd):
#         Animal.__init__(self,a,b,c,d)
#         self.weiba=w
#         self.sudu=sd
#     def run(self,foot):
#         print(self.name+'跑向'+str(foot))
#     def greet(self):
#         print(self.name+'叫')
# class Cat(Animal):
#     def __init__(self,a,b,c,d,w,sd):
#         Animal.__init__(self,a,b,c,d)
#         self.weiba=w
#         self.sudu=sd
#     def run(self,foot):
#         print(self.name+'跑向'+str(foot))
#     def greet(self):
#         print(self.name+'叫')

class vehicle():
    def __init__(self,a,b,c):
        self.speed=a
        self.king=b
        self.color=c
    def setColor(self,color):
        self.color=color
    def getColor(self):
        return self.color

class Car(vehicle):
    def __init__(self,a,b,c,p):
        vehicle.__init__(self,a,b,c)
        self.passenger=p
    def getMaxspeed(self,speed):
        print('最高速度：'+str(speed))
a=Car('60km/h','小汽车','珠光红',5)
print(a.speed,a.king,a.color,a.passenger)
a.getMaxspeed('180km/h')
a.setColor('黑色')
print(a.getColor())