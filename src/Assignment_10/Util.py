import numpy

def avg(n, marks, name):
    for i in range(n):
        lis=marks[name]
        ag=numpy.average(lis)
        return (ag)