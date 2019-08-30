import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://qzone.qq.com/")

driver.implicitly_wait(10)
driver.switch_to.frame("login_frame")
driver.find_element_by_id("img_out_1260242849").click()#点击头像登录
driver.find_element_by_link_text('好友动态').click()
# def scroll_foot(driver):
#     if driver.name == "chrome":
#        js = "var q=document.body.scrollTop=1000000"
#     else:
#       js = "var q=document.documentElement.scrollTop=1000000"
#     return driver.execute_script(js)
js="window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(js)
time.sleep(1)
js="window.scrollTo(0,0)"
driver.execute_script(js)
time.sleep(1)
a=driver.find_elements_by_css_selector("i[class='fui-icon icon-op-praise']")
for i in a:
    i.click()
    time.sleep(2)
