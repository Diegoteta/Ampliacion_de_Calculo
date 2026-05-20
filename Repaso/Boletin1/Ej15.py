import numpy as np
a=np.array([0,0])
b=np.array([1/10,1/20])
def f(p):
    x,y=p
    return np.exp(x)*np.sin(y)
def gradf_ex(p):
    x,y=p
    dx=np.exp(x)*np.sin(y)
    dy=np.exp(x)*np.cos(y)
    return np.array([dx,dy])
def gradf_num(p):
    h=1e-10
    dx=(f((p[0]+h,p[1]))-f(((p[0],p[1]))))/h
    dy=(f((p[0],p[1]+h))-f(((p[0],p[1]))))/h
    return np.array([dx,dy])
def P_ex(p,c):
    return f(c)+gradf_ex(c)@(p-c)
def P_num(p,c):
    return f(c)+gradf_num(c)@(p-c)

print('Aprox_ex = ',P_ex(b,a))
print('Aprox_num = ',P_num(b,a))