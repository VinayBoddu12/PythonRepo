import unittest
from src.Assignment_12 import Util

def mergge_the_tools(string,k):
    s=string
    n=len(s)
    for i in range(0,n,k):
        substring=s[i:i+k]
        distinct_substring=""
        for j in substring:
            if j not in distinct_substring:
                distinct_substring=distinct_substring+j
        print(distinct_substring)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        mtools=mergge_the_tools("aacdfghij", 3)
        self.assertEqual(Util.merge_the_tools("aacdfghij",3),mtools)  # add assertion here


if __name__ == '__main__':
    unittest.main()
