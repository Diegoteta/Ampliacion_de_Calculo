import numpy as np
a=np.array([2., 1.])
def f(x, y):
    return x**2+y**2-x*y-3*x
def grad_f(x, y):
    d_fx = 2*x-y-3
    d_fy = 2*y-x 
    return np.array([d_fx, d_fy])


#jacobiana=hesiana de la función
def Jgradf(x, y):
    d2_fx2 = 2
    d2_fy2 = 2
    d2_fxy = -1
    return np.array([[d2_fx2, d2_fxy], [d2_fxy, d2_fy2]])
#linealizamos y resolvemos para conocer ptos críticos
tol=1e-2
grid_xy=np.linspace(-3,3,50)
sol=np.empty((0,2),dtype=float)
for x in grid_xy:
    for y in grid_xy:
        if (np.abs(np.linalg.det(Jgradf(x,y)))>1e-10):
            z=np.linalg.solve(Jgradf(x,y),-grad_f(x,y))
            val=[x+z[0],y+z[1]]
            #compruebo si es solucion
            if (np.linalg.norm(grad_f(val[0],val[1]))<tol):
                sol=np.append(sol,[val],axis=0)
sol=np.unique(np.round(sol,1),axis=0)
print("Puntos críticos encontrados:", sol)

def grad2_f(x, y):
    d2_fx2 = 2
    d2_fy2 = 2
    d2_fxy = -1
    return np.array([[d2_fx2, d2_fxy], [d2_fxy, d2_fy2]])
print()
#lagrangiana

def grad_L(x, y, l):
    d_Lx = 2*x-y-3-2*l*x
    d_Ly = 2*y-x-2*l*y
    d_Ll = x**2+y**2-9
    return np.array([d_Lx, d_Ly, d_Ll])
def j_grad_L(x, y, l):
    d2_Lxx = 2-2*l
    d2_Lyy = 2-2*l
    d2_Lll = 0
    d2_Lxy = -1
    d2_Lxl = 2*x
    d2_Lyl = 2*y
    return np.array([[d2_Lxx, d2_Lxy, d2_Lxl], [d2_Lxy, d2_Lyy, d2_Lyl], [d2_Lxl, d2_Lyl, d2_Lll]])
tol=1e-2
grid_xy=np.linspace(0,5,100)
grid_l=np.linspace(0,5,100)
sol1=np.empty((0,3),dtype=float)
for x in grid_xy:
    for y in grid_xy:
        for l in grid_l:
            if (np.abs(np.linalg.det(j_grad_L(x,y,l)))>1e-10):
                z=np.linalg.solve(j_grad_L(x,y,l),-grad_L(x,y,l))
                val=[x+z[0],y+z[1],l+z[2]]
                #compruebo si es solucion
                if (np.linalg.norm(grad_L(val[0],val[1],val[2]))<tol):
                    sol1=np.append(sol1,[val],axis=0)
sol1=np.unique(np.round(sol1,1),axis=0)
print("Puntos críticos encontrados lagrangiana:", sol1)
print(grad_L(1,1,1)); print(); print(j_grad_L(1,1,1))