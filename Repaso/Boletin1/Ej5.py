import numpy as np
def f(p):
    x,y=p
    return x**2*y+np.exp(x*y)
def gradf(p):
    x,y=p
    fx=2*x*y+y*np.exp(x*y)
    fy=x**2+x*np.exp(x*y)
    return np.array([fx,
                     fy])
a=np.array([1,0])
b=np.array([1.2,-0.1])
def P(a,b):
    return f(a)+gradf(a)@(b-a)
print(P(a,b))
