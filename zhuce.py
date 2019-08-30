import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
#1.打开47.107.178.45网站
driver.get('http://47.107.178.45/phpwind/')
#2.点击注册
driver.find_element_by_css_selector("a.btn.btn_big.btn_error").click()
#3.输入用户名，密码，确认密码，输入邮箱
#用户名
driver.find_element_by_css_selector("input#J_reg_username.input.length_4.J_reg_input").send_keys("xiguagua")
#密码
driver.find_element_by_css_selector("input#J_reg_password.input.length_4").send_keys("123456")
#确认密码
driver.find_element_by_css_selector("input#J_reg_repassword.input.length_4").send_keys("123456")
#输入邮箱
driver.find_element_by_css_selector("input#J_reg_email.input.length_4").send_keys("111288645@qq.com")
#4.点击确定
driver.find_element_by_css_selector("button.btn.btn_big.btn_submit.mr20").click()
#进入板块
driver.find_element_by_xpath("//li[2]/a").click()
#进入帖子
driver.find_element_by_xpath("//h3/a").click()
#发帖
driver.find_element_by_css_selector("a.btn_post.J_thread_post_btn").click()
#输入标题
driver.find_element_by_css_selector("input#J_atc_title.input.length_6.mr15").send_keys("123456")
#输入内容
driver.find_element_by_xpath("///html/body").send_keys("123456")
#点击发帖
driver.find_element_by_css_selector("button#J_post_sub.btn_submit.btn_big.fl.mr10").click()
#5.退出
#5.返回首页
driver.find_element_by_xpath("//div[2]/p/a").click()