import numpy as n

def ultra():
    myarr=n.array([[4,2],[2,5],[3,7],[1,3],[4,0]])
    min=n.min(myarr,axis=1)
    return(n.max(min))
