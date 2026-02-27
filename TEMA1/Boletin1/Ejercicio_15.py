import numpy as np
a = np.array([0,0]); b = np.array([1/10,1/20])
def f(a):
    x, y = a
    return np.exp(x)*np.sin(y)
def gradf(a):
    x, y = a
    df_x = np.exp(x)*np.sin(y)
    df_y = np.exp(x)*np.cos(y)
    return np.array([df_x,df_y])
def P(b):
    x, y =b
    return f(a) + np.dot(gradf(a),(b-a))
print('Aprximacion de f(1/10,1/20) = ',P(b))