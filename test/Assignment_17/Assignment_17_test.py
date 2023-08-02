import unittest
from src.Assignment_17 import Util
import re

def validdateemail():
    def validemail(email):
        p = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
        return re.match(p, email)


    n = int(input())
    emails = [input().strip() for _ in range(n)]
    valid_emails = list(filter(validemail, emails))
    valid_emails.sort()

    print(valid_emails)


class MyTestCase(unittest.TestCase):
    def test_something(self):

        self.assertEqual(Util.validateemail(),validdateemail())  # add assertion here

if __name__ == '__main__':
    unittest.main()
