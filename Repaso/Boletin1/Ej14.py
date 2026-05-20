import numpy as np
a=np.array([1,2])
b=np.array([1.1,1.9])
def f(p):
    x,y=p
    return x**3+y**3-6*x*y
def gradf_ex(p):
    x,y=p
    dx=3*x**2-6*y
    dy=3*y**2-6*x
    return np.array([dx,dy])
def gradf_num(p):
    x,y=p
    h=1e-10
    dx=(f((p[0]+h,p[1]))-f((p[0],p[1])))/h
    dy=(f((p[0],p[1]+h))-f((p[0],p[1])))/h
    return np.array([dx,dy])
def P_ex(p,c):
    return f(c)+gradf_ex(c)@(p-c)
def P_num(p,c):
    return f(c)+gradf_num(c)@(p-c)
print('Aprox_ex = ',P_ex(b,a))
print('Aprox_num = ',P_num(b,a))