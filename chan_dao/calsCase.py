import unittest
from chan_dao import calc

class myTest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def testSum01(self):
        self.assertEqual(3,calc.sum(1,2))
    def testSum02(self):
        self.assertEqual(3,calc.sum(2,2))
    def testsub01(self):
        self.assertEqual(1,calc.sub(2,1))
    def testsub02(self):
        self.assertEqual(1,calc.sub(2,2))
if __name__=='__main__':
    unittest.main()