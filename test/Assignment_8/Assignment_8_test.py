import unittest
from src.Assignment_8 import Util
import numpy as n
def ultramain():
   my_array = n.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
   print(n.floor(my_array))
   print(n.ceil(my_array))
   print(n.rint(my_array))

class MyTestCase(unittest.TestCase):
    def test_something(self):
        # input=
#         output=[1. 2. 3. 4. 5. 6. 7. 8. 9.]
# [ 2.  3.  4.  5.  6.  7.  8.  9. 10.]
# [ 1.  2.  3.  4.  6.  7.  8.  9. 10.]
        self.assertEqual(Util.ultra(), ultramain())  # add assertion here


if __name__ == '__main__':
    unittest.main()
