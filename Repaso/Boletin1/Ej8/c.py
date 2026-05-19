import numpy as np
def f(p):
    x,y=p
    return (x**2+3*x*y+y**2)/(x**2+y**2)**(1/2)

def fx_ex(p):
    x,y=p
    return (x**3+x*y**2+3*y**2)/(x**2+y**2)**(3/2)

def fx_num(p):
    x,y=p
    h=1e-10
    return  (f((p[0]+h,p[1]))-f((p[0],p[1])))/h

print(f((1,1)))
print();print()

print(fx_ex((1,1)))  # Derivada exacta respecto a x
print();print()

print(fx_num((1, 1)))  # Derivada numérica respecto a x
