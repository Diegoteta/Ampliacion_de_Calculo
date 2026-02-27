import numpy as np
c = [0,0]
x_eval = [0.1,0.1]

def f(x, y):
    return x * np.cos(y) + y * np.sin(x)
def grad_f(x, y):
    df_dx = np.cos(y) + y * np.cos(x)
    df_dy = -x * np.sin(y) + np.sin(x)
    return np.array([df_dx, df_dy])
def Hf(x, y):
    df_xx = -y * np.sin(x)
    df_yy = -x * np.cos(y)
    df_xy = -np.sin(y) + np.cos(x)
    return np.array([[df_xx, df_xy], 
                     [df_xy, df_yy]])
def P(punto_x, punto_c):
    x, y = punto_x
    a, b = punto_c
    h = np.array([x-a, y-b])
    fa = f(a, b)
    ga = grad_f(a, b)
    Ha = Hf(a, b)
    t1 = ga @ h
    t2 = 0.5 * (h @ Ha @ h)
    return fa + t1 + t2
print('P(0.1,0.1) = ',P(x_eval,c).round(4))




    
    