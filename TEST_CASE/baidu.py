# import socks
# import socket
# socks.set_default_proxy(socks.HTTP, '地址', 25, True, '15573706812@163.com', 'zhl19980625')
# socket.socket = socks.socksocket
from selenium import webdriver
from TEST_CASE import youjian
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
    HtmlFile = "C:\\Users\\Administrator\\PycharmProjects\\untitled2\\TEST_CASE\\result.html"
    fp = open(HtmlFile, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"百度测试报告", description=u"用例测试情况")
    runner.run(testunit)
    fp.close()
    youjian.send_email(HtmlFile)