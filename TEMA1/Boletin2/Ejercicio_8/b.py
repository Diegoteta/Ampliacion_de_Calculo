import numpy as np
def grad_L(x,y,z,l):
    Lx = 1-2*x*l; Ly = 1-2*y*l; Lz = 2+l; Ll = -x**2-y**2+z
    return np.array([Lx,Ly,Lz,Ll])
def H_L(x,y,z,l):
    Lxx = -2*l; Lxy = 0; Lxz = 0; Lxl = -2*x
    Lyx = 0; Lyy = -2*l; Lyz = 0; Lyl = -2*y
    Lzx = 0; Lzy = 0; Lzz = 0; Lzl= 1
    Llx = -2*x; Lly = -2*y; Llz = 1; Lll= 0
    return ([[Lxx,Lxy,Lxz,Lxl],
             [Lyx,Lyy,Lyz,Lyl],
             [Lzx,Lzy,Lzz,Lzl],
             [Llx,Lly,Llz,Lll]])
tol = 1e-2
sol = np.empty((0,4),dtype=float)
grid_xyz = np.linspace(-0.5,0.5,5)
grid_l = np.linspace(-5,5,5)
for x in grid_xyz:
    for y in grid_xyz:
        for z in grid_xyz:
            for l in grid_l:
                if (np.abs(np.linalg.det(H_L(x,y,z,l)))>1e-10):
                    c = np.linalg.solve(H_L(x,y,z,l),-grad_L(x,y,z,l))
                    val = np.array([x+c[0],y+c[1],z+c[2],l+c[3]])
                    if (np.linalg.norm(grad_L(val[0],val[1],val[2],val[3]))<tol):
                        sol = np.append(sol,[val],axis=0)
sol = np.unique(np.round(sol,3),axis=0)
print('Puntos criticos aproximados',sol)
