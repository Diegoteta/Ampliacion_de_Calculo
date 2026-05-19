import numpy as np
def  g(p):
    x,y,z=p
    return z**2
def PHI1(p):
    theta,phi=p
    x=2*np.cos(theta)*np.sin(phi)
    y=2*np.sin(theta)*np.sin(phi)
    z=2*np.cos(phi)
    return np.array([x,y,z])
def PHI1_theta(p):
    theta,phi=p
    x=-2*np.sin(theta)*np.sin(phi)
    y=2*np.cos(theta)*np.sin(phi)
    z=0
    return np.array([x,y,z])
def PHI1_phi(p):
    theta,phi=p
    x=2*np.cos(theta)*np.cos(phi)
    y=2*np.sin(theta)*np.cos(phi)
    z=-2*np.sin(phi)
    return np.array([x,y,z])

a=0; b=2*np.pi
c=0; d=np.pi/3
n=50
dtheta=(b-a)/n
dphi=(d-c)/n
theta=np.linspace(a,b,n+1)
phi=np.linspace(c,d,n+1)
I_num1=0
for i in range(0,n):
    for j in range(0,n):
        p=np.array([theta[i],phi[j]])
        T_theta=PHI1_theta(p)
        T_phi=PHI1_phi(p)
        N=np.cross(T_theta,T_phi)
        I_num1+=g(PHI1(p))*np.linalg.norm(N)*dtheta*dphi
I_ex1=28*np.pi/3
print('I_num1 : ',I_num1)
print('I_ex1 : ',I_ex1)
print('Error1',abs(I_num1-I_ex1))

def PHI2(p):
    r,theta=p
    x=r*np.cos(theta)
    y=r*np.sin(theta)
    z=1
    return np.array([x,y,z])
def PHI2_r(p):
    r,theta=p
    x=np.cos(theta)
    y=np.sin(theta)
    z=0
    return np.array([x,y,z])
def PHI2_theta(p):
    r,theta=p
    x=-r*np.sin(theta)
    y=r*np.cos(theta)
    z=0
    return np.array([x,y,z])

a=0; b=np.sqrt(3)
c=0; d=2*np.pi
n=50
dr=(b-a)/n
dtheta=(d-c)/n
r=np.linspace(a,b,n+1)
theta=np.linspace(c,d,n+1)
I_num2=0
for i in range(0,n):
    for j in range(0,n):
        p=np.array([r[i],theta[j]])
        T_r=PHI2_r(p)
        T_theta=PHI2_theta(p)
        N=np.cross(T_r,T_theta)
        I_num2+=g(PHI2(p))*np.linalg.norm(N)*dr*dtheta
I_ex2=3*np.pi
print('I_num2 : ',I_num2)
print('I_ex2 : ',I_ex2)
print('Error2',abs(I_num2-I_ex2))

print('I_num_total : ',I_num1+I_num2)