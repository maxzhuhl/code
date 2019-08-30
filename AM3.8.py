import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(100)
url='https://www.baidu.com'
#1.打开浏览器
driver.get(url)
driver.maximize_window()
#2.搜索数据
driver.find_element_by_css_selector("input#kw").send_keys("12306")
driver.find_element_by_css_selector("input#su").click()
time.sleep(3)
#3.关闭浏览器