"""Consider the following:

A string, , of length  where .
An integer, , where  is a factor of .
We can split  into  substrings where each substring, , consists of a contiguous block of  characters in . Then, use each  to create string  such that:

The characters in  are a subsequence of the characters in .
Any repeat occurrence of a character is removed from the string such that each character in  occurs exactly once. In other words, if the character at some index  in  occurs at a previous index  in , then do not include the character in string .
Given  and , print  lines where each line  denotes string.

Input Format

The first line contains a single string, .
The second line contains an integer, , the length of each substring.

STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3
Sample Output

AB
CA
AD
"""

#
def merge_the_tools(string,k):
    s=string
    n=len(s)
    for i in range(0,n,k):
        substring=s[i:i+k]
        distinct_substring=""
        for j in substring:
            if j not in distinct_substring:
                distinct_substring=distinct_substring+j
        print(distinct_substring)