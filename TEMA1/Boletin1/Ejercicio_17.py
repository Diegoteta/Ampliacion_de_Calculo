import numpy as np
a = np.array([2,0.5])

def F(a):
    x,y=a
    f1 = x**2 + y**2 -5
    f2 = x*y - 1
    return np.array([f1,f2])
def J(a):
    x,y = a
    def grad_f1(a):
        return np.array([2*x,2*y])
    def grad_f2(a): 
        return np.array([y,x])
    return np.array([grad_f1(a),grad_f2(a)])
#Metodo Newton linealizado
delta = np.linalg.solve(J(a),-F(a))
xfinal= a + delta
print('x1 = ',xfinal)
print('Residuo = ',F(xfinal))