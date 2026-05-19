import numpy as np

def g(p):
    x,y,z=p
    return z**2
def Phi(p):
    theta,phi=p
    x=2*np.sin(phi)*np.cos(theta)
    y=2*np.sin(phi)*np.sin(theta)
    z=2*np.cos(phi)
    return np.array([x,y,z])
def Phi_theta(p):
    theta,phi=p
    x=-2*np.sin(phi)*np.sin(theta)
    y=2*np.sin(phi)*np.cos(theta)
    z=0
    return np.array([x,y,z])
def Phi_phi(p):
    theta,phi=p
    x=2*np.cos(phi)*np.cos(theta)
    y=2*np.cos(phi)*np.sin(theta)
    z=-2*np.sin(phi)
    return np.array([x,y,z])

a=0;b=2*np.pi
c=0;d=np.pi/3
n=50
dtheta=(b-a)/(n)
dphi=(d-c)/(n)
theta=np.linspace(a,b,n+1)
phi=np.linspace(c,d,n+1)

I_num=0
for i in range(0,n):
    for j in range(0,n):
        p=np.array([theta[i],phi[j]])
        T_theta=Phi_theta(p)
        T_phi=Phi_phi(p)
        N=np.cross(T_theta,T_phi)
        I_num+=g(Phi(p))*np.linalg.norm(N)*dtheta*dphi
I_ex=28*np.pi/3
print('I_num : ',I_num)
print('I_ex : ',I_ex)
