import  time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.maximize_window()
driver.implicitly_wait(10)
#1.alter 只能接受
# driver.find_element_by_id("alert").click()
# time.sleep(2)
# driver.switch_to.alert.accept()
# #2.confirm 两种操作 ：接受，取消
# driver.find_element_by_id("confirm").click()
# time.sleep(2)
# driver.switch_to.alert.dismiss()
# #3.prompt 接受、取消、输入
# driver.find_element_by_id("prompt").click()
# time.sleep(1)
# driver.switch_to.alert.send_keys("123456")
#4text


#层级定位
#1.先审查通过，过2s后复审通过
# driver.find_element_by_id("status").find_element_by_css_selector("option[value='1']").click()
# time.sleep(2)
# driver.find_element_by_id("status").find_element_by_css_selector("option[value='2']").click()

#js脚本练习
#1.执行简单的js脚本
driver.find_element_by_css_selector("input#kw").send_keys("新梦想IT教育")
# js="alter(\"祝大家找到满意工作\")"
# driver.execute_script(js)
# time.sleep(3)
driver.switch_to.alert.accept()
#2.通过js脚本获取元素的属性
js="return document.getElementById(\"kw\").value"
str=driver.execute_script(js)
name = driver.execute_script("return document.getElementById(\"kw\").name");
str2=driver.execute_script("return document.getElenmentById(\"kw\").getAttribute(\"id\").name");
print(str);
print(name);
print(str2);
#3.通过js操作滚动条
js="window.scrollBy(0,500)";
driver.execute_script(js);
time.sleep(2)
js="window.scrollBy(0,1000)";
driver.execute_script(js);
time.sleep(2)
js="window.scrollBy(0,-800)";
driver.execute_script(js);
#4.自己封装滚动条
def scroll(driver,height):
    js="window.scrollBy(0,"+height+")";
    driver.execute_script(js);
scroll(driver,"500")
time.sleep(1)
scroll((driver,"600"))
time.sleep(1)
scroll(driver,"600")
time.sleep(1)
scroll(driver,"-800")
#5.通过js的修改对象的属性，禅道提交bug 把下拉框属性改为可见