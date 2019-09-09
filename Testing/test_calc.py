import unittest
import sys
sys.path.append('../Programming')
import calc

class TestCalc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Setup class')
        cls.a = 10
        cls.b = 5

    @classmethod
    def tearDownClass(cls):
        print('Teardown class')

    def setUp(self):
        print('Setup')

    def tearDown(self):
        print('Teardown')

    def test_add(self):
        self.assertEqual(calc.add(self.a, self.b), 15)

    def test_sub(self):
        self.assertEqual(calc.sub(self.a, self.b), 5)

    def test_div(self):
        self.assertEqual(calc.div(self.a, self.b), 2)


if __name__ == '__main__':
    unittest.main()