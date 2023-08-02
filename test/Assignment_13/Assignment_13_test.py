import unittest
from src.Assignment_13 import Util

def hackerrankk_logo(thickness):
    c = 'H'

    for i in range(thickness):
        print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))
    for i in range((thickness + 1) // 2):
        print((c * thickness * 5).center(thickness * 6))

    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

    for i in range(thickness):
        print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(
            thickness * 6))

class MyTestCase(unittest.TestCase):
    def test_something(self):
        hack=hackerrankk_logo(5)
        self.assertEqual(Util.hackerrank_logo(5), hack)  # add assertion here


if __name__ == '__main__':
    unittest.main()
