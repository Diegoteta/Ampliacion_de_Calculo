import numpy as np
a=np.array([0,0,1]); b=np.array([0.02,-0.01,1.03])
def F(p):
    x,y,z=p
    return np.array([x*np.exp(y)+z,
                     y*np.exp(x)+z**2])
def J_ex(p):
    x,y,z=p
    return np.array([[np.exp(y),x*np.exp(y),1],
                     [y*np.exp(x),np.exp(x),2*z]])
def P_ex(p,c):
    return F(c)+J_ex(c)@(p-c)
print('Aprox_ex = ',P_ex(b,a))

def J_num(p):
    x,y,z=p
    h=1e-10
    dx=(F((p[0]+h,p[1],p[2]))-F((p[0],p[1],p[2])))/h
    dy=(F((p[0],p[1]+h,p[2]))-F((p[0],p[1],p[2])))/h
    dz=(F((p[0],p[1],p[2]+h))-F((p[0],p[1],p[2])))/h
    return np.array([dx,dy,dz]).T

def P_num(p,c):
    return F(c)+J_num(c)@(p-c)
print('Aprox_num = ',P_num(b,a))
