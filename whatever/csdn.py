import time
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
driver=webdriver.Chrome()#导入谷歌浏览器驱动
driver.maximize_window()#窗口最大化
driver.get("http://www.baidu.com")#输入网址
print(driver.title)
driver.implicitly_wait(10)#隐式等待10秒
driver.find_element_by_id("kw").send_keys("csdn")#定位输入框输入参数
driver.find_element_by_id("su").click()#点击百度一下
default_window=driver.window_handles # #获取所有句柄
print(default_window)
driver.switch_to.window(default_window[0]) #切换句柄
driver.find_element_by_xpath("//*[@id=1]/h3/a[1]").click()#点击csdn首页
default_window=driver.window_handles # #获取所有句柄
print(default_window)
driver.switch_to.window(default_window[1]) #切换句柄
#driver.find_element_by_css_selector("#nav-left-menu > li:nth-child(6) > a").click()#点击论坛
driver.find_element_by_css_selector("#toolber-keyword").send_keys("123")#输入框输入搜索的内容
driver.find_element_by_css_selector("#csdn-toolbar > div > div > ul > li:nth-child(2) > div > a").click()#点击搜索按钮
default_window=driver.window_handles #获取所有句柄
print(default_window)
driver.switch_to.window(default_window[2]) #切换句柄
driver.find_element_by_css_selector("body > div.main-container > div.con-l > div.search-list-con > dl:nth-child(2) > dt > div > a").click()#选择第一个搜索内容
time.sleep(2)
default_window=driver.window_handles #获取所有句柄
print(default_window)
driver.switch_to.window(default_window[3]) #切换句柄
driver.execute_script('document.documentElement.scrollTop=10000')
# 10000表示一下拉到底
time.sleep(10)
# driver.find_element_by_css_selector("#mainBox > main > div.recommend-box > div.recommend-end-box > p > a").click()#点击返回首页
print(driver.title)
