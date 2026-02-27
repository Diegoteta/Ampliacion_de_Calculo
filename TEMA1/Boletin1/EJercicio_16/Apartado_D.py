import numpy as np

a = np.array([0,0,1]); b = ([0.02,-0.01,1.03])

def F(a):
    x,y,z = a
    f1 = x*np.exp(y) + z
    f2 = y*np.exp(x) + z**2
    return np.array([f1,f2])

def grad_f1(a):
    x,y,z = a
    df1_x = np.exp(y)
    df1_y = x*np.exp(y)
    df1_z = 1
    return np.array([df1_x,df1_y,df1_z])

def grad_f2(a):
    x,y,z = a
    df2_x = y*np.exp(x)
    df2_y = np.exp(x)
    df2_z = 2*z
    return np.array([df2_x,df2_y,df2_z])

def J(a):
    return np.array([grad_f1(a),grad_f2(a)])

def P(a,b):
    return F(a)+ np.dot(J(a),(b-a))
print(P(a,b))
