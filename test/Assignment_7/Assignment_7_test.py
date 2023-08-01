import unittest
from src.Assignment_7 import Util

def pprint_formatted(number):
    for i in range(1,number+1):
        hex_value = "{0:x}".format(i)
        print(i," ",oct(i)[2:]," ", hex_value," ", bin(i)[2:])

class MyTestCase(unittest.TestCase):
    def test_something(self):
        input=6
#         output=1   1   1   1
# 2   2   2   10
# 3   3   3   11
# 4   4   4   100
# 5   5   5   101
# 6   6   6   110
        self.assertEqual(Util.print_formatted(input), pprint_formatted(6))  # add assertion here


if __name__ == '__main__':
    unittest.main()
