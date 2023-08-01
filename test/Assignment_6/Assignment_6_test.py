import unittest
from src.Assignment_6 import Util

# def mutated_string(string, position, character):
#     ls=list(string)
#     ls[position]=
#     str=""
#     for i in ls:
#         str=str+i
#     return str

class MyTestCase(unittest.TestCase):
    def test_something(self):
        # input=("vinayboddu",5,"k")
        output="vinaykoddu"
        self.assertEqual(Util.mutate_string("vinayboddu",5,'k'), output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
