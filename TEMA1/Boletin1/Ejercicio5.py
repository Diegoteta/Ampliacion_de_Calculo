import matplotlib.pyplot as plt
import numpy as np
# Crear una figura y un eje 3D  
fig = plt.figure()
ax =fig.add_subplot(111, projection='3d')

x=np.linspace(0,2,50)
y=np.linspace(-1,1,50)
X,Y=np.meshgrid(x,y)

def z(x,y): 
    return x**2*y+np.exp(x*y)
a=[1,0]
b=[1.2,-0.1]
def P(x,y): 
    def gradf(x,y):
        return np.array([2*x*y+np.exp(x*y)*y,x**2+np.exp(x*y)*x])
    gradf0=gradf(a[0],a[1])
    return gradf0[0]*(x-a[0])+gradf0[1]*(y-a[1])+z(a[0],a[1])

print('f(a)=',z(a[0],a[1]),'P(a)=',P(a[0],a[1]),'error=',abs(z(a[0],a[1])-P(a[0],a[1])))
print()
print('f(b)=',z(b[0],b[1]),'P(b)=',P(b[1],b[1]),'error=',abs(z(b[0],b[1])-P(b[0],b[1])))

ax.plot_surface(X,Y,z(X,Y))
ax.plot_surface(X,Y,P(X,Y),alpha=0.5)
ax.scatter(a[0], a[1], z(a[0], a[1]), color='red', s=100, edgecolors='black')
plt.show()


