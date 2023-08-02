from src.Assignment_15.Util import *

n, m = map(int, input().split())
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

res = happiness(arr, A, B)
print(res)