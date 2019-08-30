import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(100)
driver.get('http://192.168.0.251/index.php')
driver.find_element_by_id("zentao").click()#点击开源版
driver.find_element_by_id("account").send_keys("zzz")#输入账户
driver.find_element_by_name("password").send_keys("123456")#密码
driver.find_element_by_id("submit").click()#登录
driver.find_element_by_link_text("项目").click()#点击项目
driver.find_element_by_link_text("Bug").click()#点击bug
driver.find_element_by_link_text("提Bug").click()#点击提交bug
driver.find_element_by_xpath("//*[@id='module_chosen']/a/span").click()#所属模块
#driver.find_element_by_css_selector("option[value=\'2\']").click()
driver.find_element_by_xpath("//*[@id='module_chosen']/div/ul/li[3]").click()
time.sleep(2)
#当前指派
driver.find_element_by_id("assignedToBox").click()
driver.find_element_by_css_selector('#assignedTo_chosen > div > ul > li:nth-child(2)').click()
time.sleep(2)
#driver.find_element_by_css_selector("a[class='chosen-single chosen-default']").click()#指派用户
# driver.find_element_by_css_selector("a[title=\'zzz\']").click()
#影响版本
driver.find_element_by_xpath('//*[@id="openedBuild_chosen"]/ul').click()
driver.find_element_by_xpath('//*[@id="openedBuild_chosen"]/div/ul/li[2]').click()
time.sleep(2)
driver.find_element_by_id("type").click()#选择bug类型
driver.find_element_by_css_selector("option[value=\'interface\']").click()#选择界面显示
time.sleep(1)
driver.find_element_by_id("os").click()#选择操作系统
driver.find_element_by_css_selector("option[value=\'all\']").click()#选择全部
time.sleep(1)
driver.find_element_by_id("browser").click()#选择浏览器
driver.find_element_by_css_selector("option[value=\'ie\']").click()#选择ie
#driver.find_element_by_css_selector("a[class='btn dropdown-toggle']").click()#bug标题颜色
driver.find_element_by_id("title").send_keys("页面错误")#bug标题
time.sleep(1)
#优先级
driver.find_element_by_xpath('//*[@id="dataform"]/table/tbody/tr[5]/td/div[2]/div[2]/div/div[2]').click()
driver.find_element_by_xpath('//*[@id="dataform"]/table/tbody/tr[5]/td/div[2]/div[2]/div/div[2]/ul/li[4]/a').click()
#步骤重现
f=driver.find_element_by_xpath('//*[@id="dataform"]/table/tbody/tr[6]/td/div[2]/div[2]/iframe')
driver.switch_to.frame(f)
driver.find_element_by_xpath('/html/body').clear()
driver.find_element_by_xpath('/html/body').send_keys(""
                                                     "[步骤]w！！\n"
                                                     "[结果]e\n"
                                                     "[期望]rue\n")
driver.switch_to.default_content()
time.sleep(1)
#抄送
driver.find_element_by_id("mailto_chosen").click()
driver.find_element_by_css_selector('#mailto_chosen > div > ul > li:nth-child(3)').click()
time.sleep(1)
#关键词
driver.find_element_by_id("keywords").send_keys('bug')
#标题
#driver.find_element_by_xpath('//*[@id="mailto"]/option[4]').send_keys('SSS')
#time.sleep(1)
#driver.find_element_by_id("dataform").click()#点击外面
#提交表单
driver.find_element_by_css_selector("form#dataform").submit()