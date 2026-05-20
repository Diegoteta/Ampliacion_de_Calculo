import numpy as np
def W(p):
    x,y=p
    return 2*(x**2+y**2)*(x/y)
def gradW_ex(p):
    x,y=p
    return 2*np.array([3*x**2/y+y,-x**3/y**2+x])
def gradW_num(p):
    x,y=p
    h=1e-10
    dx_num=(W((p[0]+h,p[1]))-W((p[0],p[1])))/h
    dy_num=(W((p[0],p[1]+h))-W((p[0],p[1])))/h
    return np.array([dx_num,dy_num])

print('Grad_ex = ',gradW_ex((1,1)))
print('Grad_num = ',gradW_num((1,1)))
    