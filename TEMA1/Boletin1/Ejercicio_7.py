import numpy as np
def gradU(x,y):
    du_x=x/(x**2+y**2+1)**(3/2)
    du_y=y/(x**2+y**2+1)**(3/2)
    return -np.array([du_x,du_y])
print(gradU(1,0))