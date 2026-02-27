import numpy as np
p = np.array([0, 0, 1]); a=np.array([2,3,1]); ap=a-p
u=ap/np.linalg.norm(ap) #NORMALIZAMOS VECTOR 
def gradT(p):
    x, y, z = p
    dt_x = 10 * np.exp(-y**2) - 20 * x * z * np.exp(-x**2)
    dt_y = -20 * x * y * np.exp(-y**2)
    dt_z = 10 * np.exp(-x**2)
    return np.array([dt_x, dt_y, dt_z])
print('Gradiente en p ',gradT(p))
print('Direccional en direccion u ',np.dot(gradT(p),u))

