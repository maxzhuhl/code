# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# import time,os,unittest
#
# class baidu(unittest.TestCase):
#     def setUp(self):
#         Chromedi="C:\2018年selenium自动化测试实习工具\chromedriver.exe"
#         os.environ["webdriver.Chrome.driver"]=Chromedi
#         self.driver=webdriver.Chrome(Chromedi)
#         self.baseurl="https://www.baidu.com"
#         self.verificationErrors=[]
#         self.accpet_next_alter=True
#     def test_baidu_set(self):
#         driver=self.driver
#         driver.maximize_window()
#         driver.get(self.baseurl+"/")
#         m=driver.find_element_by_id("tj_briicon")
#         ActionChains(driver).move_to_element(m).perform()
#         driver.find_element_by_partial_link_text("知道").click()
#         # self.assertEqual(driver.current_url,"http://zhidao.baidu.com/")
#         self.assertEqual(driver.title, u"百度知道 - 全球最大中文互动问答平台")
#         time.sleep(2)
#
#         def tearDown(self):
#             self.driver.quit()
#
#         if __name__ == "__main__":
#             unittest.main()

# import os
# caselist=os.listdir('C:\Users\Administrator\PycharmProjects\untitled2\lianxi')
# for a in caselist:
#     s=a.split('.')[-1]
#     if s=='py':
#         os.system('oython C:\Users\Administrator\PycharmProjects\untitled2\lianxi\%s 1>>log.txt 2>&1'%a)
from selenium import webdriver
from lianxi import youjian
import unittest
import time, sys
import HTMLTestRunner
import smtplib
smtpObj=smtplib.SMTP()
reload = (sys)

class Baidu(unittest.TestCase):
    """百度首页搜索测试用例"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.baidu.com"
        print('123')
    def test_baidu_search(self):
        driver = self.driver
        print
        u"========【case_0001】 百度搜索============="
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(u"林志玲")
        driver.find_element_by_id("su").click()
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        # 必须要打印路径HTMLTestRunner才能捕获并且生成路径，\image\**.png 是获取路径的条件，必须这样的目录
        pic_path = '..\\result\\image\\' + now + '.png'
        driver.save_screenshot(pic_path)
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    # now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    testunit = unittest.TestSuite()
    testunit.addTest(Baidu("test_baidu_search"))
    now = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
    HtmlFile = "C:\\Users\\Administrator\\PycharmProjects\\untitled2\\lianxi\\result.html"
    fp = open(HtmlFile, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"百度测试报告", description=u"用例测试情况")
    runner.run(testunit)
    fp.close()
    youjian.send_email(HtmlFile)