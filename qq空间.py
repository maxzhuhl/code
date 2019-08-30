import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("https://qzone.qq.com/")

driver.implicitly_wait(10)
driver.switch_to.frame("login_frame")
driver.find_element_by_id("img_out_1260242849").click()#点击头像登录
# driver.find_element_by_id("switcher_plogin").click()#选择账号密码登录
# driver.find_element_by_id("u").send_keys("1260242849")#输入账号
# driver.find_element_by_id("p").send_keys("")#密码
# driver.find_element_by_id("login_button").click()#点击登录
#driver.find_element_by_id("$1_substitutor_content").send_keys(Keys.CONTROL,'v')
driver.find_element_by_id("$1_substitutor_content").send_keys('自动化测试')
driver.find_element_by_link_text("发表").click()
