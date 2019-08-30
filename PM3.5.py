#键盘操作事件
# import time
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# driver=webdriver.Chrome()
# driver.get("https://www.baidu.com")
#1.普通键 table键
# driver.find_element_by_name("wd").click()
# time.sleep(3)
#百度一下 按tab跳 新闻
# driver.find_element_by_css_selector("input#kw").send_keys(Keys.TAB)
#2.组合键:粘贴
# driver.find_element_by_css_selector("input#kw").send_keys(Keys.CONTROL,'v')
#3.关闭窗口
# time.sleep(3)
# driver.find_element_by_css_selector("input#kw").send_keys(Keys.ALT,Keys.F4)

#验证并打印信息
# time.sleep(2)
# tit=driver.title
# if tit==u"百度一下，你就知道":
#     print ('title is ok')
# else:
#     print('title is no !!')

#定位一组对象
#1.往所有的input输入“我爱代码，代码让我充实”
# time.sleep(3)
# inputs=driver.find_elements_by_css_selector("input.c-input")
# for e1 in inputs:
#     e1.send_keys("我爱代码，代码使我快乐")


#层级定位
import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.implicitly_wait(10)
driver.find_element_by_link_text("登录").click()
driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()
driver.find_element_by_id("TANGRAM__PSP_10__userName").\
    find_element_by_id("TANGRAM__PSP_10__userName").send_keys("15573706812")
driver.find_element_by_id("TANGRAM__PSP_10__password").\
    find_element_by_id("TANGRAM__PSP_10__password").send_keys("123")
driver.find_element_by_id("TANGRAM__PSP_10__submit").click()
