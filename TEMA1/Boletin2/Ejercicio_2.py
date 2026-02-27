import numpy as np
c = [0,0]
x_eval = [0.1,-0.1]
def f(x,y):
    return np.sqrt(1+x)*np.sqrt(1+y)
def grad_f(x,y):
    df_x = 1/2*(np.sqrt(1+y)/np.sqrt(1+x))
    df_y = 1/2*(np.sqrt(1+y)/np.sqrt(1+x))
    return np.array([df_x,df_y])
def H_f(x,y):
    df_xx = -1/4*(np.sqrt(1+y)/np.sqrt(1+x)**3)
    df_xy = 1/4*(1/(np.sqrt(1+x)*np.sqrt(1+y)))
    df_yy = -1/4*(np.sqrt(1+x)/np.sqrt(1+y)**3)
    return np.array([[df_xx,df_xy]
                    ,[df_xy,df_yy]])
def P2(punto_x,punto_c):
    x,y = punto_x
    a,b = punto_c
    h = np.array([x-a,y-b])
    fc = f(a,b); grad_fc = grad_f(a,b); H_fc = H_f(a,b)
    t1 = grad_fc@h; t2 = h@H_fc@h
    return fc + t1 + 1/2*t2
print('P2(0.1,-0.1) = ',P2(x_eval,c).round(4))