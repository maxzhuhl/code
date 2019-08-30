import unittest
class test(unittest.TestCase):
        flag=True
        def test1(self):
            print("执行测试用例1");
            self.assertEqual(3,3);
        def test2(self):
            print("执行测试用例2");
            self.assertTrue(1==1);
        def test3(self):
            print("执行测试用例3");
            self.assertGreater(5,4);
def suite():
    suite=unittest.TsetSuite()
    suite.addTest(test('test2'))
    suite.addTest(test('test3'))
    return suite
if __name__ == "__main__":
       unittest.main(defaultTest='suite')