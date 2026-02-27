import numpy as np
def f(x, y):
    return np.sqrt(1+x)*np.sqrt(1+y)
def fx(x, y):
    return 0.5*np.sqrt(1+y)/np.sqrt(1+x)    
def fy(x, y):
    return 0.5*np.sqrt(1+x)/np.sqrt(1+y)
def fxx(x, y):
    return -0.25*np.sqrt(1+y)/np.power(1+x,1.5)
def fyy(x, y):
    return -0.25*np.sqrt(1+x)/np.power(1+y,1.5)
def fxy(x, y):
    return 0.25/np.sqrt(1+x)/np.sqrt(1+y)
#Polinomio de Taylor de orden 2ç
x0=0
y0=0
def taylor2(x, y, x0, y0):
    return f(x0, y0) + fx(x0, y0)*(x-x0) + fy(x0, y0)*(y-y0) + 0.5*fxx(x0, y0)*(x-x0)**2 + 0.5*fyy(x0, y0)*(y-y0)**2 + fxy(x0, y0)*(x-x0)*(y-y0)
print("Polinomio de Taylor de orden 2 en (0.1,-  0.1):", taylor2(0.1, -0.1, x0, y0))