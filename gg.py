import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
#1.打开47.107.178.45网站
driver.get('http://47.107.178.45/phpwind/')
#2.输入用户名，密码
driver.find_element_by_css_selector('input[id="J_username"]').send_keys('xiguagua')
driver.find_element_by_css_selector('input[id="J_password"]').send_keys('123456')
#3.点击登录
driver.find_element_by_css_selector('button[id="J_sidebar_login"]').click()
time.sleep(5)#等待5s 再进入板块
#进入板块
driver.find_element_by_css_selector('#J_header > nav > div > ul > li:nth-child(2) > a').click()
#进入帖子
driver.find_element_by_css_selector('body >'
' div > div.main_wrap > div > div.box_wrap > div:nth-child(3) > div.ct '
'> table > tbody > tr:nth-child(1) > th > h3 > a').click()
#发帖
driver.find_element_by_css_selector('body >'
' div > div.main_wrap > div.main.cc > div.main_body > div > div:nth-child(6) > a').click()
driver.find_element_by_css_selector('input[name="atc_title"][id="J_atc_title"]').send_keys('zhuzhu')
driver.switch_to.default_content() #回到默认窗口
#将帖子框架赋值给g
g=driver.find_element_by_xpath('//*[@id="mainForm"]/div/nav/nav/div/div[3]/div[1]/div/div/div[2]/iframe')
driver.switch_to.frame(g) #切换到内容窗口
#输入帖子内容
driver.find_element_by_css_selector('html body.editor_content').send_keys('what')
driver.switch_to.default_content()#回到默认窗口
#点击发布
driver.find_element_by_css_selector('button[name="Submit"][class="btn btn_submit btn_big fl mr10"]').click()
time.sleep(20)
driver.quit()
#selenium中的断言函数