#浏览器操作
import time
from selenium import webdriver

#浏览器操作练习
#创建一个驱动
driver = webdriver.Chrome()
#1.打开百度
driver.get('https://www.baidu.com')
# driver.find_element_by_name("tj_trhao123").click()
# 2.窗口最大化
# driver.maximize_window()
# 3.刷新，点击hao123等待5s刷新
# time.sleep(5)
# driver.refresh()
# 4.后退
# time.sleep(2)
# driver.back()
# 5.前进，回到hao123
# time.sleep(2)
# driver.forward()
# 6.等待3s后截图
# time.sleep(3)
# driver.get_screenshot_as_file("c:\\客户端\.png")
# 7.获取当前的URL标题
# url=driver.current_url
# title=driver.title
# print(url,title)
# 8.退出quit()和close()的区别
# driver.quit()

#第二章练习
# 1.通过id定位元素
#driver.find_element_by_id("kw").send_keys("12306")
# 2.通过name定位元素
# 3.通过class——name定位元素，百度一下
# 4.通过tag_name定位元素
# 5.通过link定位
# time.sleep(3)
# driver.find_element_by_partial_link_text("hao").click()

# 1.通过绝对路径做定位
#driver.find_element_by_css_selector("html body div#wrapper div#head div.head_wrapper div#u1 a+a").click()
# driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/a[2]").click()
# 2.通过相对路径做定位
# driver.find_element_by_xpath("//div[3]/a[2]").click()
# driver.find_element_by_xpath("//*[@id=\"u1\"]/a[2]").click()
# 3.通过元素索引定位，索引的初始值为1
#4.使用xpath属性定位
#driver.find_element_by_xpath("//a[@name='tj_trnews']").click()
# driver.find_element_by_xpath("//a[@name='tj_trtieba']").click()
# driver.find_element_by_xpath()

#css
#1.使用绝对路径定位元素
#driver.find_element_by_css_selector("html body div#wrapper div#head div.head_wrapper div#u1 a+a").click()
#2.使用相对路径来定位元素
# driver.find_element_by_css_selector("div#u1 a+a").click()
# 3.定位下节点 +
#4.使用相对id选择来定位元素
#5.使用属性选择器来定位元素
#属性[1='值']属性2=['值']
# driver.find_element_by_css_selector("a[name='ti_trhao123']").click()
# driver.find_element_by_css_selector("a[name='tj_trhao123'][class='mnav']").click()
#6.部分属性值的匹配
#匹配开始
# driver.find_element_by_css_selector("a[name^='tj_trh'][class='mnav']").click()
#匹配结束
# driver.find_element_by_css_selector("a[name$='hao123'][class='mnav']").click()
#任意匹配
# driver.find_element_by_css_selector("a[name*='hao'][class='mnav']").click()
#7.列表选择具体的匹配（下标）
# driver.find_element_by_css_selector("a[class='mnav']:nth-of-type(3)").click()
