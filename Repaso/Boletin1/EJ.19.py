import numpy as np 
def g(p):
    u,v=p
    return np.array([u**2+v,np.exp(u),u*v])
def J_g(p):
    h=1e-10
    du=(g((p[0]+h,p[1]))-g((p[0],p[1])))/h
    dv=(g((p[0],p[1]+h))-g((p[0],p[1])))/h
    return np.array([du,dv]).T

def F(p):
    x,y,z=p
    return np.array([x*y+z,y+np.exp(z)])
def J_F(p):
    h=1e-10
    dx=(F((p[0]+h,p[1],p[2]))-F((p[0],p[1],p[2])))/h
    dy=(F((p[0],p[1]+h,p[2]))-F((p[0],p[1],p[2])))/h
    dz=(F((p[0],p[1],p[2]+h))-F((p[0],p[1],p[2])))/h
    return np.array([dx,dy,dz]).T

def J_H(p):
    return J_F(g(p))@J_g(p)
print(J_H((0,2)))