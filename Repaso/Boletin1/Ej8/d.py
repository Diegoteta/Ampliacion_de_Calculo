import numpy as np
def f(p):
    x,y=p
    return (x**2-y**2)**1/2

def fx_ex(p):
    x,y=p
    return x/(x**2-y**2)**(1/2)
def fy_ex(p):
    x,y=p
    return y/(x**2-y**2)**(1/2)

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

print(fx_ex((1,-2)))  # Derivada exacta respecto a x
print(fy_ex((2,0)))  # Derivada exacta respecto a y
print();print()

print(fx_num((1, -2)))  # Derivada numérica respecto a x
print(fy_num((2, 0)))  # Derivada numérica respecto a y