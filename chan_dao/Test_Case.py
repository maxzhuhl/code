import unittest
from chan_dao import  calc
class test_case1(unittest.TestCase):
    def setUp(self):
        print("执行前置条件")
        pass
    def tearDown(self):
        print("执行后置代码，清场")
        pass
    def test_sum1(self):
        print("执行用例1")
        self.assertEqual(calc.sum(1,2),3,"通过测试")
    def test_sum2(self):
        print("执行用例2")
        self.assertEqual(calc.sum(1,2),2,"测试失败")
    def test_sub(self):
        print("执行用例3")
        self.assertEqual(10-5,6)  #断言

def suite():
    suite=unittest.TestCase();
    suite.addTest(test_case1("test_sum1"));
    suite.addTest(test_case1("test_sum2"));
    return  suite
if __name__=="__main__":
    unittest.main(defaultTest='suite')