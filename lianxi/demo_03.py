import unittest
import time
from selenium import webdriver
class test1(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.baidu.com")
    def tearDown(self):
        time.sleep(2)
        self.driver.quit()
    # def testTitle(self):
    #     self.driver.finnd_element_by_css_selector("inout#kw").send_key("新梦想软件测试")
    #             time.sleep(2)
    #             title=self.driver.title
    #             self.assertEqual(title,"新梦想软件测试_百度一下")
if __name__=="__main__":
    unittest.main()