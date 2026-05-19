import numpy as np
def f(p):
    r,theta=p
    return r*(3-r**2-2*r*np.cos(theta))

nr=200
ntheta=200

theta=np.linspace(0,2*np.pi,ntheta+1); dtheta=(2*np.pi-0)/ntheta
r=np.linspace(0,1,nr+1); dr=(1-0)/nr
I1=0
for i in range(0,ntheta):
    thetac=theta[i]+dtheta/2
    for j in range(0,nr):
        rc=r[j]+dr/2
        I1+=f([rc,thetac])*dtheta*dr
I1_ex=5*np.pi/2
print('integrar primer tramo exc',I1_ex)
print('integrar primer tramo num',I1)
print('errrorm primer tramo',abs(I1-I1_ex))
