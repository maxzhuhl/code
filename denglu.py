import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
#1.打开47.107.178.45网站
driver.get('http://47.107.178.45/phpwind/')
#2.输入用户名，密码
driver.find_element_by_css_selector("input#J_username.input").send_keys("admin")
driver.find_element_by_css_selector("input#J_password.input").send_keys("123456")
#3.点击登录
driver.find_element_by_css_selector("button#J_sidebar_login.btn.btn_big.btn_submit").click()
#4.发帖
# driver.find_element_by_css_selector("div#J_header.header.cc li+a")
#进入板块
driver.find_element_by_xpath("//li[2]/a").click()
#进入帖子
#driver.find_element_by_xpath("h3/a").click()
driver.find_element_by_link_text("selenium").click()
#点击发帖
# driver.find_element_by_xpath("//div[3]/a").click()
driver.find_element_by_css_selector("a.btn_post.J_thread_post_btn").click()
#输入标题
driver.find_element_by_css_selector("input#J_atc_title.input.length_6.mr15").send_keys("123456")
#输入内容
driver.find_element_by_xpath("///html/body").send_keys("123456")
#点击发帖
driver.find_element_by_css_selector("button#J_post_sub.btn_submit.btn_big.fl.mr10").click()
#5.退出
#driver.find_element_by_css_selector("html body div#J_header div#J_header_user_menu div.header_menu.my_menu.cc a+a").click()
#driver.close()
