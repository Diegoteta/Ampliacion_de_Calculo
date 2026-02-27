import numpy as np
def L_grad_L(x, y, l):
    d_Lx = 2*x*(1-l)-y-3
    d_Ly = 2*y*(1-l)-x
    d_Ll = -x**2-y**2+9
    return np.array([d_Lx, d_Ly, d_Ll])
def j_L_grad_L(x, y, l):
    d2_Lxx = 2*(1-l)
    d2_Lxy = -1
    d2_Lxl = -2*x

    d2_Lyx = -1
    d2_Lyy = 2*(1-l)       
    d2_Lyl = -2*y
    
    d2_Llx = -2*x
    d2_Lly = -2*y
    d2_Lll = 0
    
    return np.array([[d2_Lxx, d2_Lxy, d2_Lxl], 
                     [d2_Lyx, d2_Lyy, d2_Lyl], 
                     [d2_Llx, d2_Lly, d2_Lll]])
tol=1e-2
grid_xy=np.linspace(0,5,50)
grid_l=np.linspace(0,5,50)
sol1=np.empty((0,3),dtype=float)
for x in grid_xy:
    for y in grid_xy:
        for l in grid_l:
            if (np.abs(np.linalg.det(j_L_grad_L(x,y,l)))>1e-10):
                z=np.linalg.solve(j_L_grad_L(x,y,l),-L_grad_L(x,y,l))
                val=[x+z[0],y+z[1],l+z[2]]
                #compruebo si es solucion
                if (np.linalg.norm(L_grad_L(val[0],val[1],val[2]))<tol):
                    sol1=np.append(sol1,[val],axis=0)
sol1 = np.unique(np.round(sol1, 1), axis=0)
print("Puntos críticos encontrados lagrangiana:", sol1)