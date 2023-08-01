import unittest
from src.Assignment_11 import Util
import datetime
def cal():
    date = str(input())
    days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    day=datetime.datetime.strptime(date,"%d %m %y").weekday()
    print(days[day])


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(Util.call(), cal())  # add assertion here


if __name__ == '__main__':
    unittest.main()
