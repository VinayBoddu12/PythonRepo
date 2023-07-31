import unittest
from src.Assignment_4 import Util


def ultramain(input):
    list = []
    b = list[:]
    list.insert(0, 5)
    list.insert(1, 10)
    list.insert(0, 6)
    print(list)
    list.remove(6)
    list.append(9)
    list.append(1)
    list.sort()
    print(list)
    list.pop()
    list.reverse()
    print(list)

class MyTestCase(unittest.TestCase):
    def test_something(self):
        input=12
        # expected=[6, 5, 10]
        # [1, 5, 9, 10]
        # [9, 5, 1]
        self.assertEqual(Util.main(input),ultramain(input))  # add assertion here




if __name__ == '__main__':
    unittest.main()
