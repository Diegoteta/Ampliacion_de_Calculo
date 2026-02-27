import numpy as np
x_eval = np.array([1/4,1/2])
c = np.array([0,0])
def f(x,y):
    return np.log(x + np.exp(y))
def grad_f(x,y):
    df_x = 1/(x + np.exp(y))
    df_y = np.exp(y)/(x + np.exp(y))
    return np.array([df_x,df_y])
def H_f(x,y):
    df_xx = -1/(x + np.exp(y))**2
    df_xy = -np.exp(y)/(x + np.exp(y))**2
    df_yy = x*np.exp(y)/(x + np.exp(y))**2
    return np.array([[df_xx,df_xy],
                     [df_xy,df_yy]])
def P2(punto_x,punto_c):
    x,y = punto_x
    a,b = punto_c
    h = np.array([x-a,y-b])
    fc = f(a,b); grad_fc = grad_f(a,b); H_fc = H_f(a,b)
    t1 = grad_fc@h
    t2 = h@H_fc@h
    return fc + t1 +1/2*t2
print('P(0.25,0.5)',P2(x_eval,c))
