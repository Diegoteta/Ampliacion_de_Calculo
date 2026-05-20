import numpy as np

def F(p):
    x,y=p
    return np.array([x**2+y**2-5,
                     x*y-1])
def J(p):
    x,y=p
    return np.array([[2*x,2*y],
                     [y,    x]])
x0=np.array([2,0.5])
for n in range(10):
    delta=np.linalg.solve(J(x0),-F(x0))
    x0=x0+delta
print('x1 = ',x0)
print('F(x1) = ',F(x0))
