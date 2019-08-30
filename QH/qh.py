import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.maximize_window()#窗口最大化
driver.get("http://www.baidu.com/")#打开浏览器到东富龙网址
driver.implicitly_wait(10)
driver.find_element_by_id("kw").send_keys("can协议")
driver.find_element_by_id("su").click()
#driver.find_element_by_id("content_02_02_clear").click()
# driver.find_element_by_id("zd_name").send_keys("MLC001")#输入账号
# time.sleep(2)
# driver.find_element_by_id("zd_name02").send_keys("qwert123")#输入密码
# time.sleep(2)
# driver.find_element_by_id("content_02_02_submit").click()#点击登录
# time.sleep(2)
# driver.find_element_by_id("homepage").click()#点击个人主页，进入到个人主页
# time.sleep(2)
# driver.switch_to_frame("mainDiv_0_x")#框架跳转
# driver.find_element_by_xpath("/html/body[1]/div/ul/li[1]").click()
# driver.switch_to_frame("mainDiv_2_x")#框架跳转
# driver.switch_to.default_content()#退出框架
# time.sleep(2)
# driver.find_element_by_id("personMana").click()