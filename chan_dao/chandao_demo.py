#读取csv文件
import csv
csv_file=csv.reader(open('c:\\userinfo.csv','r'))
print(csv_file)
# content=[]
for line in csv_file:
    print(line)
#写入csv文件
# csv_file=csv.writer(open('c:\\userinfo.csv','a'))
# print(csv_file)
# item1=['userp','55555','22','12484@qq.com']
# item2=['userpm','555s55','2s2','1248s4@qq.com']
# csv_file.writerow(item1)
# csv_file.writerow(item2)