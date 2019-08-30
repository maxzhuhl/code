import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
# driver.get('http://47.107.178.45/phpwind/')
driver.get('file:///D:/%E4%B8%8A%E8%AF%BE%E8%B5%84%E6%96%99/%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95/Wait.html')
#返回对象的尺寸
#size=driver.find_element_by_css_selector("#J_username").size
#获取对象的文本
#text=driver.find_element_by_css_selector("a.sendpwd").text
#获取对象标签名称
#result=driver.find_element_by_id("head_checkbox").tag_name
# time.sleep(2)
# tit=driver.title
# if tit==u"百度一下，你就知道":
#     print ('title is ok')
# else:
#     print('title is no !!')
#尺寸
# username_input=driver.find_element_by_name("username")
# size=username_input.size
# print(size)
#文本
# print(driver.find_element_by_link_text('找回密码').text)
#属性名
# print(username_input.get_attribute("classs"))
# print(username_input.get_attribute("name"))
# print(username_input.get_attribute("id"))
#是否可见
# print('是否可见:%s'%(username_input.is_displayed()))
#是否给禁用
# print('是否被禁用：%s'%(username_input.is_enabled()))
#是否被选中
# driver.find_element_by_name("rememberme").click()
# print(driver.find_element_by_name("rememberme").is_selected())
#标签名称
# print(driver.find_element_by_name("rememberme").tag_name)
# print(username_input.tag_name)
#鼠标操作
#1.鼠标右击
# wl=driver.find_element_by_id("su")
#ActionChains动作链条
# ActionChains(driver).context_click(wl).perform()
# time.sleep(3)
#释放鼠标
# ActionChains(driver).release().perform()
#2.鼠标悬停 百度->设置->高级设置
# wl=driver.find_element_by_xpath("//div[3]/a[8]")
# ActionChains(driver).move_to_element(wl).perform()
# driver.find_element_by_link_text("高级搜索").click()

# 隐私等待
driver.implicitly_wait(10)
def highLightElement(driver,element):
 driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",
                         element,"background:green ;border:2px solid red;")
#等待时间操作
#1.不加任何等待，不能识别到元素，直接报错
driver.find_element_by_id("b").click()
wl=driver.find_element_by_class_name("red_box")
wl.click()

#2. 强制等待6秒
driver.find_element_by_id("b").click()
time.sleep(6)
wl=driver.find_element_by_class_name("red_box")
highLightElement(driver,wl)

#3.关闭强制等待，设置隐私等待， 隐私等待只需要设置一次
driver.find_element_by_id("b").click()
wl=driver.find_element_by_class_name("red_box")
highLightElement(driver.wl)
#4.类强制等待，关闭隐私等待
# from selenium.webdriver.support.ui import WebDriverWait
#driver.find_element_by_id("b").click()
#引入WebDriverWait类
el=WebDriverWait(driver,10).until(lambda x: x.find_element_by_class_name("red_box"))
highLightElement(driver,el)-[]