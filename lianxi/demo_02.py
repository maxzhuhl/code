import unittest
import time, sys
import io
import HTMLTestRunner
from lianxi import youjian
class test(unittest.TestCase):
        flag=True
        def test1(self):
            print("执行测试用例1");
            self.assertEqual(3,3);
        def test2(self):
            print("执行测试用例2");
            self.assertTrue(1==1);
        @unittest.skipIf(0,'跳过')
        def test3(self):
            print("执行测试用例3");
            self.assertGreater(5,4);
if __name__ == "__main__":
    suite=unittest.TestSuite()
    suite.addTest(test('test2'))
    suite.addTest(test('test3'))
    now = time.strftime("%Y-%m-%d_%H_%M_%S",time.localtime(time.time()))
    filename="C:\\Users\\Administrator\\PycharmProjects\\untitled2\\lianxi\\testresult.html"
    fp=open(filename,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"测试执行用例",description=u'用例执行情况')
    runner.run(suite)
    fp.close()
    youjian.send_email(filename)