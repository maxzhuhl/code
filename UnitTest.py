import unittest
import time
from selenium import webdriver
class test1(unittest.TestCase):
    def setUp(self):#前置初始化
        self.driver=webdriver.Chrome();
        self.driver.get("https://www.baidu.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    def tearDown(self):
        time.sleep(2)
        self.driver.quit()
    def testTitle(self):
        self.driver.find_element_by_id('kw').send_keys("12306")
        time.sleep(2)
        title=self.driver.title;
        #加断言
        self.assertAlmostEqual(title,'12306_百度搜索')
#执行用例
if __name__=='__main__':
    unittest.main()