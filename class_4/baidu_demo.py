import time
from selenium import webdriver
url="https://www.baidu.com"
1#打开浏览器，获取驱动  线性脚本
driver=webdriver.Chrome()
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(10)
#2.搜索数据
driver.find_element_by_css_selector("input#kw").send_keys("12306")
time.sleep(1)
driver.find_element_by_css_selector("input#su")
time.sleep(1)
#3.关闭浏览器
driver.quit()