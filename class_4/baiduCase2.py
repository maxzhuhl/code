from class_4.open_web import openwed
from class_4.search import search
from class_4.quit import quit

url="https://www.baidu.com"
#数据驱动脚本2，数据放TXT文件
caseDate=open('testDate.txt','r',encoding='UTF-8');
searchs=caseDate.readlines()
print(searchs)
for str in searchs:
    driver=openwed(url)
    driver=search(driver,str)
    quit(driver)