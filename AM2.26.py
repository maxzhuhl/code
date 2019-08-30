#读文件操作
#1.安装对应的软件 2.文件的路径 3.操作
#python自带有解析txt文件的软件（工具包）
#读
# import os
# filePath = os.getcwd()+'/test.txt'
# txtfile = open(filePath,'r',encoding='UTF-8')
# txtline = txtfile.readlines()#readline读一行 +s读取多行
# txtline = txtfile.readlines(2)#读一行，一行中的几个字符
# txtline = txtfile.read(2)#读取n个字符
# txtline = (txtfile.readlines()[1][:-1])
# print(txtline)
#read函数的特性
#使用read函数一次后，文件指针会指向当前read函数操作完的下一个位置
# print(txtfile.readline())
# print(txtfile.readline())
# print(txtfile.read(1))
# print(txtfile.read())
#写文件操作
import os
filePath = os.getcwd()+'/test.txt'
txtfile = open(filePath,'r',encoding='UTF-8')
# txtfile.write('nn')
# txtfile.write(',xiangming')
# txtfile.write('\n')#换行重新写
# txtfile.write('chifanlema')
# txtfile.flush()
# print(txtfile.writable())#判断文件是否可写
# txtfile.writelines(['aaa','bbb'])#可以写入列表
#文件位置操作
#tell seek函数
print(txtfile.read(3))
print(txtfile.tell())#显示当前文件指针的位置
txtfile.seek(2)#改变文件指针的位置
print(txtfile.tell())
print(txtfile.read(2))
print(txtfile.tell())
txtfile.seek(0,0)#0偏移量 0 位置（0开头，1当前，2结尾）
print(txtfile.read(2))
txtfile.seek(2,1)
print(txtfile.read(2))
#写文件
# wfilePath = os.getcwd()+'/wtest.txt'
# wtxt = open(wfilePath,'w')
# wtxt.write('xiaoming')
# wtxt.flush()#把数据同步到磁盘
# wtxt.close()

# atxt = open(wfilePath,'a',encoding='UTF-8')
# atxt.write('赵dd我儿子')
# atxt.flush()
# atxt.close()