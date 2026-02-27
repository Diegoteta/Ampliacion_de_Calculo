import numpy as np
c = [0,0]
x_eval = [1/10,1/20]

def f(x,y):
    return np.exp(x)*np.sin(y)

def grad_f(x,y):
    df_x = np.exp(x)*np.sin(y)
    df_y = np.exp(x)*np.cos(y)
    return np.array([df_x,df_y])

def H_f(x,y):
    df_xx = np.exp(x)*np.sin(y)
    df_xy = np.exp(x)*np.cos(y)
    df_yy = -np.exp(x)*np.sin(y)
    return np.array([[df_xx,df_xy],
                     [df_xy,df_yy]])

def P2(punto_x,punto_c):
    x,y = punto_x
    a,b = punto_c
    h = np.array([x-a,y-b])
    fc = f(a,b)
    grad_fc = grad_f(a,b)
    H_fc = H_f(a,b)
    t1 = grad_fc@h; t2 = h@H_fc@h
    return fc + t1 +1/2*t2
print('P(0.1,0.05)',P2(x_eval,c).round(4))