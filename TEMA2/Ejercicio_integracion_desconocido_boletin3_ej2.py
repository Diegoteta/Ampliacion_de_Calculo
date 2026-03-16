import numpy as np
def f(p):
    x,y=p
    return x*y
nx=200
ny=200
x=np.linspace(-2,0,nx+1); dx=(0-(-2))/nx
y=np.linspace(0,2,ny+1); dy=(2-0)/ny
I1=0
for i in range(0,nx):
    xc=x[i]+dx/2
    for j in range(0,ny):
        yc=y[j]+dy/2
        if (0<=yc<=xc+2):
            I1+=f([xc,yc])*dx*dy
I1_ex=-2/3
print('integrar primer tramo exc',I1_ex)
print('integrar primer tramo num',I1)
print('errrorm primer tramo',abs(I1-I1_ex))



x=np.linspace(0,3,nx+1); dx=(3-0)/nx
y=np.linspace(0,2,ny+1); dy=(2-0)/ny
I2=0
for i in range(0,nx):
    xc=x[i]+dx/2
    for j in range(0,ny):
        yc=y[j]+dy/2
        if (0<=yc<=2/3*np.sqrt(9-xc**2)):
            I2+=f([xc,yc])*dx*dy
I2_ex=9/2
print('integrar segundo tramo exc',I2_ex)
print('integrar segundo tramo num',I2)
print('errrorm segundo tramo',abs(I2-I2_ex))


