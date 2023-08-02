import unittest
from src.Assignment_14 import Util
import calendar as c

def find_day(month, day, year):
    days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
    day_of_week = c.weekday(year, month, day)
    return days[day_of_week]

class MyTestCase(unittest.TestCase):
    def test_something(self):
        days=find_day(8,2,2023)
        self.assertEqual(Util.finding_day(8,2,2023), days)  # add assertion here


if __name__ == '__main__':
    unittest.main()
