import numpy as np
def gradF(p):
    x,y=p
    fx=x/(x**2+y**2+1)**(3/2)
    fy=y/(x**2+y**2+1)**(3/2)
    return np.array([fx,fy])
def F(p):
    return -gradF(p)
print(F(np.array([1,0])))
