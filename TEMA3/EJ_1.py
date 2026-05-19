import numpy as np
def g(p):
    x,y,z=p
    return x+y**2
def Phi(p):
    theta,z=p
    x=2*np.cos(theta)
    y=2*np.sin(theta)
    z=z
    return np.array([x,y,z])
def Phi_theta(p):
    theta,z=p
    x=-2*np.sin(theta)
    y=2*np.cos(theta)
    z=z
    return np.array([x,y,z])
def Phi_z(p):
    theta,z=p
    x=0
    y=0
    z=1
    return np.array([x,y,z])
a=0;b=3
c=0;d=2*np.pi
n=50
dtheta=(d-c)/n
dz=(b-a)/n
theta=np.linspace(d,c,n+1)
z=np.linspace(a,b,n+1)
I_num=0
for i in range(0,n):
    for j in range(0,n):
        p=np.array([theta[i],z[j]])
        T_theta=Phi_theta(p)
        T_z=Phi_z(p)
        N=np.cross(T_theta,T_z)
        I_num+=g(Phi(p))*np.linalg.norm(N)*dtheta*dz
I_ex=24*np.pi
print('I_num : ',I_num)
print('I_ex : ',I_ex)
print('Error',abs(I_num-I_ex))