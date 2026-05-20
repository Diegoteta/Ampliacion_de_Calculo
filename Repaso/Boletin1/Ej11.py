import numpy as np
e=np.exp
a=np.array([0,0,1])
b=np.array([2,3,1])
r=b-a ; ru= r/np.linalg.norm(r)
def T(p):
    x,y,z=p
    return 10*(x*e(-y**2)+z*e(-x**2))

def gradT_ex(p):
    x,y,z=p
    dx=e(-y**2)-2*x*z*e(-x**2)
    dy=-2*x*y*e(-y**2)
    dz=e(-x**2)
    return 10*np.array([dx,dy,dz])

def gradT_num(p):
    x,y,z=p
    h=1e-10
    dx=(T((p[0]+h,p[1],p[2]))-T((p[0],p[1],p[2])))/h
    dy=(T((p[0],p[1]+h,p[2]))-T((p[0],p[1],p[2])))/h
    dz=(T((p[0],p[1],p[2]+h))-T((p[0],p[1],p[2])))/h
    return np.array([dx,dy,dz])

def Dr_ex(p,r):
    return gradT_ex(p)@r
def Dr_num(p,r):
    return gradT_num(p)@r

print('D_direccional_ex = ',Dr_ex(a,ru))
print('D_direccional_num = ',Dr_num(a,ru))
