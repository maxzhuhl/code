import time
from selenium import webdriver

# #1.创建一个webdriver驱动
# driver = webdriver.Chrome()
# #2.打开百度网站
# driver.get('https://www.baidu.com')
# #3.创建最大化
# driver.maximize_window()
# #4.搜索新梦想软件测试
# driver.find_element_by_name("wd").send_keys("新梦想软件测试")
# #5.点击百度一下
# driver.find_element_by_id("su").click()
# #6.sleep 秒钟
# time.sleep(3)
# #7.关闭浏览器
# driver.close()

#1.创建一个webdriver驱动
driver = webdriver.Chrome()
#2.打开百度网站
driver.get('http://47.107.178.45/phpwind/')
#3.创建最大化
driver.maximize_window()
#4.搜索http://47.107.178.45/phpwind/
#5.点击百度一下
#driver.find_element_by_id("su").click()
#6.输入账户admin'
driver.find_element_by_id("J_username").send_keys("admin")
#7.输入密码123456
driver.find_element_by_id("J_password").send_keys("123456")
#8.点击登录
driver.find_element_by_id("J_sidebar_login").click()
#9.sleep3秒钟
time.sleep(6)
#10.关闭浏览器
#driver.close()
