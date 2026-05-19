import numpy as np
def f(p):
    x,y=p
    return np.exp(x*y)+x/y+np.sin((2*x+3*y)*np.pi)

def fx_ex(p):
    x,y=p
    return y*np.exp(x*y)+1/y+2*np.pi*np.cos((2*x+3*y)*np.pi)

def fy_ex(p):
    x,y=p
    return x*np.exp(x*y)-x/y**2+3*np.pi*np.cos((2*x+3*y)*np.pi)

def fx_num(p):
    x,y=p
    h=1e-10
    return  (f((p[0]+h,p[1]))-f((p[0],p[1])))/h
def fy_num(p):
    x,y=p
    h=1e-10
    return  (f((p[0],p[1]+h))-f((p[0],p[1])))/h

print(f((1,1)))
print();print()


print(fx_ex((1,1)))  # Derivada exacta respecto a x
print(fy_ex((1,1)))  # Derivada exacta respecto a y
print();print()



print(fx_num((1, 1)))  # Derivada numérica respecto a x
print(fy_num((1, 1)))  # Derivada numérica respecto a y