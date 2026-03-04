import numpy as np
def f(p): #para evaluar si el pto cae fuera o dentro
    x,y = p
    return x**2+y**2
a=0; b=1 #def rectangulo para la rejilla, lim integracion
c=0; d=1
#rejilla en X y en Y
nx=10; ny=10 
dx=(b-a)/nx; dy=(d-c)/ny
x=np.linspace(a,b,nx+1)
y=np.linspace(c,d,ny+1)
sum=0
for i in range(nx):
    for j in range(ny):
        #calculamos el pto central del rectangulo R_IJ
        xij=x[i]+dx/2; yij=y[j]+dy/2
        cij=np.array([xij,yij]) #pto central
        if (xij**2<=yij<=xij):
            sum+=f(cij)*dx*dy
v_num=sum
v_exact=3/35
print('Volumen aproximado: ',v_num,'Volumen exacto: ',v_exact,'Error',np.abs(v_num-v_exact))
