import unittest
from src.Assignment_15 import Util

class MyTestCase(unittest.TestCase):
    def test_something(self):
        arr=[1,2,3,4,5]
        set1={2,3,4}
        set2={5,7}
        output=2
        self.assertEqual(Util.happiness(arr,set1,set2), output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
