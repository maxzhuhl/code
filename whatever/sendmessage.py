import time
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
# 或者直接从select导入
# from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com")#输入网址
print(driver.title)
driver.implicitly_wait(10)#隐式等待10秒
driver.find_element_by_id("kw").send_keys("csdn")#定位输入框输入参数
driver.find_element_by_id("su").click()#点击百度一下
default_window=driver.window_handles # #获取所有句柄
print(default_window)
driver.switch_to.window(default_window[0]) #切换句柄
driver.find_element_by_xpath("//*[@id=1]/h3/a[1]").click()#进入csdn首页
default_window=driver.window_handles
print(default_window)
driver.switch_to.window(default_window[1])
driver.find_element_by_id("blogClick").click()#点击写博客
default_window=driver.window_handles
print(default_window)
driver.switch_to.window(default_window[2])
driver.find_element_by_css_selector("#app > div > div > div > div.main-login > div.main-select > ul > li:nth-child(2) > a").click()
#账号密码登录
time.sleep(5)
driver.find_element_by_id("all").send_keys("15573706812")
#输入账户
driver.find_element_by_id("password-number").send_keys("zhl19980625")
#输入密码
driver.find_element_by_css_selector("#app > div > div > div > div.main-login > div.main-process-login > div > div:nth-child(6) > div > button").click()
#点击登录
#driver.find_element_by_css_selector("body > div.app.app--light > div.layout > div.beginnerGuide-box.show-beginnerGuide-box > div.beginnerGuide > div.middle > div.middle-hand > button").click()
#跳过提示
driver.find_element_by_css_selector("body > div.app.app--light > div.layout > div.layout__panel.layout__panel--articletitle-bar > div > div.article-bar__input-box > input").send_keys("测试")
driver.find_element_by_css_selector("body > div.app.app--light > div.layout > div.layout__panel.layout__panel--articletitle-bar > div > div.article-bar__user-box.flex.flex--row > button").click()
#点击发布
driver.find_element_by_css_selector("body > div.app.app--light > div.modal > div > div > div.modal__content > div.inline-box > div:nth-child(1) > div").click()
driver.find_element_by_css_selector("#uZvVOtQwioiGaXO1 > option:nth-child(2)").click()


