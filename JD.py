import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.jd.com/")
driver.implicitly_wait(10)
driver.find_element_by_id("key").send_keys("iphonex")
driver.find_element_by_css_selector('button[class="button"]').click()
driver.find_element_by_id("J_AD_5089253").click()
default_window=driver.window_handles # #获取所有句柄
print(default_window)
# a=driver.window_handles
# print(a)
# driver.switch_to.window(a[1])获取句柄
driver.switch_to.window(default_window[1]) #切换句柄
driver.find_element_by_link_text("加入购物车").click()
driver.find_element_by_id("GotoShoppingCart").click()
driver.find_element_by_link_text("去结算").click()
time.sleep(10)
driver.find_element_by_id('order-submit').click()



