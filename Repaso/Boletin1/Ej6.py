import numpy as np
def f(p):
    x,y=p
    return np.log(x-2*y)

def gradf(p):
    x,y=p
    fx=1/(x-2*y)
    fy=-2/(x-2*y)
    return np.array([fx,fy])
a=np.array([3,1])
b=np.array([3.1,1.05])

def P(a,b):
    return f(a)+gradf(a)@(b-a)
print(P(a,b))