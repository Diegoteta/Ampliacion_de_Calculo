import numpy as np
def f(p):
    x,y=p
    return np.sqrt(4-x**2)

def Phi(p):
    x,y=p
    return np.array([x,y,f(p)])

def Phi_x(p,dx):
    x,y=p
    p1=np.array([x+dx,y])
    Tx=Phi(p1)-Phi(p)
    return Tx

def Phi_y(p,dy):
    x,y=p
    p1=np.array([x,y+dy])
    Ty=Phi(p1)-Phi(p)
    return Ty

a=0;b=np.sqrt(3)
c=0;d=1
n=50
dx=(b-a)/(n)
dy=(d-c)/(n)
x=np.linspace(a,b,n+1)
y=np.linspace(c,d,n+1)
A_num=0
for i in range(0,n):
    for j in range(0,n):
        p=np.array([x[i],y[j]])
        T_x=Phi_x(p,dx)
        T_y=Phi_y(p,dy)
        N=np.cross(T_x,T_y)
        A_num+=np.linalg.norm(N)
A_ex=2*np.pi/3
print('A_num : ',A_num)
print('A_ex : ',A_ex)




