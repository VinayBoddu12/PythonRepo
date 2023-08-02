import unittest
from src.Assignment_16 import Util


class MyTestCase(unittest.TestCase):
    def test_something(self):
        letter="a b c"
        output=0.6667
        self.assertEqual(Util.probabilityofa(3,letter, 2), output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
