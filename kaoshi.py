import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element_by_id("kw").send_keys("新梦想软件测试")
