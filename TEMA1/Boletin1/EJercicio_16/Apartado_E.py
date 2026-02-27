import numpy as np

a = np.array([0,0,1]); b = ([0.02,-0.01,1.03])

def f1(a): 
    x,y,z=a
    return x*np.exp(y) + z
def f2(a):
    x,y,z=a
    return y*np.exp(x) + z**2
    

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
#Aproximación numerica grad_f1
def grad_f1_num(a):
    h=1e-6
    df1_x = f1([a[0]+h,a[1],a[2]])-f1([a[0],a[1],a[2]]); df1_x /=h 
    df1_y = f1([a[0],a[1]+h,a[2]])-f1([a[0],a[1],a[2]]); df1_y /=h
    df1_z = f1([a[0],a[1],a[2]+h])-f1([a[0],a[1],a[2]]); df1_z /=h
    return np.array([df1_x,df1_y,df1_z])
#Aproximacion numrica grad_f2
def grad_f2_num(a):
    h=1e-6
    df2_x = f2([a[0]+h,a[1],a[2]])-f2([a[0],a[1],a[2]]); df2_x /=h   
    df2_y = f2([a[0],a[1]+h,a[2]])-f2([a[0],a[1],a[2]]); df2_y /=h
    df2_z = f2([a[0],a[1],a[2]+h])-f2([a[0],a[1],a[2]]); df2_z /=h
    return np.array([df2_x,df2_y,df2_z])
#Aproximacion numerica jacobiana
def J_num(a):
    return np.array([grad_f1_num(a),grad_f2_num(a)])
print(J_num(a).round(1))


