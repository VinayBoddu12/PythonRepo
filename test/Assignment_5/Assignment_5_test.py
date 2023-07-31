import unittest
from src.Assignment_5.Util import *



class MyTestCase(unittest.TestCase):
    def test_something(self):
        input=[1,2,3,4,5,5]
        output=4
        self.assertEqual(main(input), output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
