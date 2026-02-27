import matplotlib.pyplot as plt
import numpy as np
# Crear una figura y un eje 3D  
fig = plt.figure()
ax =fig.add_subplot(111, projection='3d')

x=np.linspace(2.5,3.5,50)
y=np.linspace(0.5,1.2,50)
X,Y=np.meshgrid(x,y)

def z(x,y): 
    argumento = x-2*y
    return np.where(argumento > 0, np.log(argumento), np.nan)
a=[3,1]
b=[3.1,1.05]
def P(x,y): 
    def gradf(x,y):
        return np.array([1/(x-2*y),-2/(x-2*y)])
    gradf0=gradf(a[0],a[1])
    return gradf0[0]*(x-a[0])+gradf0[1]*(y-a[1])+z(a[0],a[1])

print('f(a)=',z(a[0],a[1]),'P(a)=',P(a[0],a[1]),'error=',abs(z(a[0],a[1])-P(a[0],a[1])))
print()
print('f(b)=',z(b[0],b[1]),'P(b)=',P(b[0],b[1]),'error=',abs(z(b[0],b[1])-P(b[0],b[1])))

ax.plot_surface(X,Y,z(X,Y))
ax.plot_surface(X,Y,P(X,Y),alpha=0.5)
ax.scatter(a[0], a[1], z(a[0], a[1]), color='red', s=100, edgecolors='black')
plt.show()