"""
The itertools module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination. Together, they form an iterator algebra making it possible to construct specialized tools succinctly and efficiently in pure Python.

To read more about the functions in this module, check out their documentation here.

You are given a list of  lowercase English letters. For a given integer , you can select any  indices (assume -based indexing) with a uniform probability from the list.

Find the probability that at least one of the  indices selected will contain the letter: ''.

Sample Input

4
a a c d
2

Sample Output

0.8333
"""

import itertools

def probabilityofa(n, letters, k):
    total_combinations = 0
    a_combinations = 0

    for combination in itertools.combinations(range(n), k):
        total_combinations += 1
        if any(letters[i] == 'a' for i in combination):
            a_combinations += 1

    return round(a_combinations / total_combinations,4)