import unittest
from testcase.TestCase import testCase


class testsuit(unittest.TestCase):
    def test_suit(self):
        my_suit = unittest.TestSuite()

        case_list = ['test001', 'test002']

        for case in case_list:
            my_suit.addTest(testCase(case))

        unittest.TextTestRunner(verbosity=2).run(my_suit)


if  __name__ == "__main__":
    unittest.main()