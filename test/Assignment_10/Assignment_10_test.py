import unittest
from src.Assignment_10 import Util

class MyTestCase(unittest.TestCase):
    def test_something(self):
        n=3
        student_marks={'vinay':[10,20,30],'syam':[20,30,40],'Suraj':[30,40,50]}
        query_name="syam"
        output=30
        input=Util.avg(n,student_marks,query_name)
        self.assertEqual(input, output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
