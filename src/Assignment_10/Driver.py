from src.Assignment_10.Util import *

n = int(input())
student_marks = {}
name, *line = input().split()
scores = list(map(float, line))
student_marks[name]=scores
query_name=input()
print(avg(n,student_marks,name))