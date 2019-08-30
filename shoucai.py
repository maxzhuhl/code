import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import  os
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://qzone.qq.com/")

driver.implicitly_wait(10)
driver.switch_to.frame("login_frame")
driver.find_element_by_id("img_out_1260242849").click()#点击头像登录
driver.find_element_by_css_selector('#tab_applist_show > li:nth-child(4) > a > div.qz-main > span').click()
time.sleep(5)
# ActionChains(driver).move_to_element('QQ空间').click()
driver.find_element_by_css_selector('body > div > div.app-topbar.top-fix-bar > div > a').click()