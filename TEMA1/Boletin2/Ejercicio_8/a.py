import numpy as np 
def grad_L1(x,y,l):
    Lx = y - 2*x*l; Ly = x - 2*y*l; Ll = - x**2 - y**2 + 1
    return np.array([Lx,Ly,Ll])
def H_grad_L1(x,y,l):
    Lxx = -2*l; Lxy = 1; Lxl = -2*x
    Lyx = 1; Lyy = -2*l; Lyl = -2*y
    Llx = -2*x; Lly = -2*y; Lll = 0
    return np.array([[Lxx,Lxy,Lxl],
                     [Lyx,Lyy,Lyl],
                     [Llx,Lly,Lll]])
tol1 = 1e-2
sol1 = np.empty((0,3),dtype=float)
grid_xy = np.linspace(-1,1,100)
grid_l = np.linspace(-1,1,100)
for x in grid_xy:
    for y in grid_xy:
        for l in grid_l:
            if (np.abs(np.linalg.det(H_grad_L1(x,y,l)))>1e-10):
                z = np.linalg.solve(H_grad_L1(x,y,l),-grad_L1(x,y,l))
                val = np.array([x+z[0],y+z[1],l+z[2]])
                if (np.linalg.norm(grad_L1(val[0],val[1],val[2]))<tol1):
                    sol1 = np.append(sol1,[val],axis=0)
sol1 = np.unique(np.round(sol1,1),axis=0)
print('Ptos críticos (A) = ',sol1)
