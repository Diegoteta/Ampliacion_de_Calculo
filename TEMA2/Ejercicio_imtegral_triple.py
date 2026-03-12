import numpy as np
def g(p):
    x,y,z = p
    return x**2+y**2+z**2

a=0; b=1
c=0; d=2
e=0; f=3

nx=10; ny=10; nz=10
dx=(b-a)/nx; dy=(d-c)/ny; dz=(f-e)/nz

x=np.linspace(a,b,nx+1)
y=np.linspace(c,d,ny+1)
z=np.linspace(e,f,nz+1)
sum=0
for i in range(nx):
    for j in range(ny):
        for k in range(nz):
            #calculamos el pto central del rectangulo R_IJ
            xijk=x[i]+dx/2; yijk=y[j]+dy/2; zijk=z[k]+dz/2
            cijk=np.array([xijk,yijk,zijk]) #pto central
            sum+=g(cijk)*dx*dy*dz
v_num=sum
v_exact=28
print('Volumen aproximado: ',v_num,'Volumen exacto: ',v_exact,'Error',np.abs(v_num-v_exact))