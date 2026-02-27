import numpy as np
def gradW(x,y):
    dw_x=6*(x**2/y)+2*y
    dw_y=-2*(x**3/y**2)+2*x
    return np.array([dw_x,dw_y])
print(gradW(1,1))