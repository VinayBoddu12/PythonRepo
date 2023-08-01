def mutate_string(string, position, character):
    ls=list(string)
    ls[position]=character
    str=""
    for i in ls:
        str=str+i
    return str

# s = input()
# i, c = input().split()
# s_new = mutate_string(s, int(i), c)
# print(s_new)