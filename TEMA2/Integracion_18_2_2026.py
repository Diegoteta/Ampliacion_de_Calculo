import numpy as np
def f(x,y):
    return x**2+y**2
#integral de Riemann
#rejilla (n x m)
a=0; b=1; n=100
c=0; d=2; m=200

x=np.linspace(a,b,n+1)
y=np.linspace(c,d,m+1)
sum=0
for i in range(1,n+1):
    for j in range(1,m+1):
        #area de la base
        A=(x[i]-x[i-1])*(y[j]-y[j-1])
        #altura
        c=np.array([(x[i]+x[i-1])/2,(y[j]+y[j-1])/2])
        sum+=A*f(c[0],c[1])
print("Integral de Riemann: ",sum)



        