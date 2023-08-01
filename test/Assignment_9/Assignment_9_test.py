import unittest
from src.Assignment_9 import Util

class MyTestCase(unittest.TestCase):
    def test_something(self):
        expectedoutput=3
        self.assertEqual(Util.ultra(), expectedoutput)  # add assertion here


if __name__ == '__main__':
    unittest.main()
