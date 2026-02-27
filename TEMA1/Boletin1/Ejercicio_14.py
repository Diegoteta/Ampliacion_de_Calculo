import numpy as np
a = np.array([1,2]) #pto de centrado del plano/pol de taylor grado 1
c = np.array([1.1,1.9])
def f(a):
    x, y = a
    return x**3 + y**3 - 6*x*y
def gradf(a):
    x, y = a
    df_x = 3*x**2 - 6*y
    df_y = 3*y**2 - 6*x
    return np.array([df_x,df_y])
def P(c):
    x, y = c
    return f(a)+np.dot(gradf(a),(c-a))
print('Aprximacion de f(1.1,1.9) = ',P(c))


