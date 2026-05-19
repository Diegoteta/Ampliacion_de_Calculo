import numpy as np
def f(p):
    x,y=p
    return x**2*np.tan(x*y)

def fx_ex(p):
    x,y=p
    return 2*x*np.tan(x*y)+x**2*y*1/np.cos(x*y)**2
def fy_ex(p):
    x,y=p
    return x**3*1/np.cos(x*y)**2

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