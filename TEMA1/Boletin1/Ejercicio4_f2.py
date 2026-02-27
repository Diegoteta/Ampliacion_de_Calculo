import matplotlib.pyplot as plt
import numpy as np
# Crear una figura y un eje 3D  
fig = plt.figure()
ax =fig.add_subplot(111, projection='3d')

x=np.linspace(-3,3,50)
y=np.linspace(-3,3,50)
X,Y=np.meshgrid(x,y)

def z(x,y): 
    return np.sqrt(x**2+y**2)

ax.plot_surface(X,Y,z(X,Y))
plt.show()