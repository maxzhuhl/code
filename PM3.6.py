#滚动条
import  time
from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element_by_css_selector("input#kw").send_keys("新梦想软件测试")
time.sleep(3)
#1.绝对滚动，滚动到页面的底部
# js="window.scrollTo(0,document.body.scrollHeight)"
# driver.execute_script(js)
# time.sleep(3)
ActionChains(driver).send_keys(Keys.DOWN)
# driver.find_element_by_id("id").send_keys(Keys.DOWN)
#2.绝对滚动，滚动到页面的顶部
# js="window.scrollTo(0,0)"
# driver.execute_script(js)
# time.sleep(3)

#3.相对滚：向下滚
# js="windows.scrollBy(0,500)"
# time.sleep(2)
# js="window.scrollBy(0,800)"

#4.
#5.封装一个滚动的方法
# def scroll(driver,heigh):
#     js="window.scrollBy(0,"+heigh+")";
#     driver.execute_script(js);
# scroll("800")
# time.sleep(1)
# scroll("800")
# scroll("800")
# scroll("-800")

#cookie处理
#1.获取全部的cookie信息
#


#2.删除所有cookies
# driver.delete_all_cookies()

#3.自己添加有个cookie，再查看是否添加成功
# driver.add_cookie({'domain':'www.baidu.com',
#                    'httpOnly':False,
#                    'name':'zhuhonglei',
#                    'path':'/','secure':False,
#                    'value':'12358456'})
# str=driver.get_cookies()
# print(str)
