from class_4.open_web import openwed
from class_4.search import search
from class_4.quit import quit
url="https://www.baidu.com"
driver=openwed(url)
driver=search(driver,'新梦想软件测试')
quit(driver)

driver=openwed(url)
driver=search(driver,"12306")
quit(driver)

driver=openwed(url)
driver=search(driver,"selenium")
quit(driver)