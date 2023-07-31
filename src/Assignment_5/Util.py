
def main(num):
    num.sort()
    lis=[]
    for i in num:
        if i not in lis:
            lis.append(i)
    return (lis[-2])