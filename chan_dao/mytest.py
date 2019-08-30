import unittest
from chan_dao import calc
class mytest(unittest.TestCase):
    def setUp(self):#初始化工作
        self.testnum=calc.calc(3,4)
    def tearDown(self):#退出清理工作
        del self.testnum
    def testsum(self):#具体的测试用例
        self.assertEqual(self.testnum.sum(),8,"testing sum")
        #@unittest.skip('不执行')#忽略测试用例
    def testsub(self):
        self.assertEqual(self.testnum.sub(),8,"testing sub")
        #@unittest.skip('不执行')
    def testmulti(self):#具体的测试用例
        self.assertEqual(self.testnum.multi(),8,"testing multi")
        #@unittest.skip('不执行')
def suite():
    suite=unittest.TestCase()
    suite.addTest(mytest("testsum"))
    suite.addTest(mytest("testsub"))
    return suite
if __name__=="__main":
    unittest.main(defaultTest='suite')