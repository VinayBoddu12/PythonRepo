"""There is an array of  integers. There are also  disjoint sets,  and , each containing  integers.
You like all the integers in set  and dislike all the integers in set .
Your initial happiness is 0. For each  integer in the array, if , you add  to your happiness.
If , you add  to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

Sample Input
3 2
1 5 3
3 1
5 7
Sample Output

1

"""
def happiness(arr, A, B):
    happiness = 0
    for num in arr:
        if num in A:
            happiness += 1
        elif num in B:
            happiness -= 1
    return happiness