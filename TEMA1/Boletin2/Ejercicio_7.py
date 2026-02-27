import numpy as np
def gradL(x,y,l):
    dL_x = 2*x*(1-l) - y - 3; dL_y = 2*y*(1-l) - x; dL_l = - x**2 - y**2 + 9
    return np.array([dL_x,dL_y,dL_l])
def H_gradL(x,y,l):
    dL_xx = 2*(1-l); dL_xy = -1; dL_xl = -2*x
    dL_yx = -1; dL_yy = 2*(1-l); dL_yl = -2*y
    dL_lx = -2*x; dL_ly = -2*y; dL_ll = 0
    return np.array([[dL_xx,dL_xy,dL_xl],
                     [dL_yx,dL_yy,dL_yl],
                     [dL_lx,dL_ly,dL_ll]])
tol = 1e-2
grid_xy = np.linspace(-3,3,100)
grid_l = np.linspace(0,5,50)
sol = np.empty((0,3),dtype=float)
for x in grid_xy:
    for y in grid_xy:
        for l in grid_l:
            if (np.abs(np.linalg.det(H_gradL(x,y,l)))>1e-10):
                z = np.linalg.solve(H_gradL(x,y,l),-gradL(x,y,l))
                val = np.array([x + z[0],y + z[1],l + z[2]])
                if (np.linalg.norm(gradL(val[0],val[1],val[2]))<tol):
                    sol = np.append(sol,[val],axis=0)
sol = np.unique(np.round(sol, 1), axis=0)
print("Puntos críticos encontrados lagrangiana:")
print()
print(sol)