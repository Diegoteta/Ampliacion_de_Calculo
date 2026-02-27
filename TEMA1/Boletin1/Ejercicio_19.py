import numpy as np 
def g(u,v):
    return np.array([u**2 + v,np.exp(u),u*v])

def JF_num(x,y,z): 
    h=1e-10
    def F1(x,y,z):  
        return x*y + z
    def F2(x,y,z):  
        return y + np.exp(z)
    dF1_x = F1(x+h,y,z)-F1(x,y,z); dF1_x /=h 
    dF1_y = F1(x,y+h,z)-F1(x,y,z); dF1_y /=h
    dF1_z = F1(x,y,z+h)-F1(x,y,z); dF1_z /=h
    grad_F1 = np.array([dF1_x,dF1_y,dF1_z])

    dF2_x = F2(x+h,y,z)-F2(x,y,z); dF2_x /=h 
    dF2_y = F2(x,y+h,z)-F2(x,y,z); dF2_y /=h
    dF2_z = F2(x,y,z+h)-F2(x,y,z); dF2_z /=h
    grad_F2 = np.array([dF2_x,dF2_y,dF2_z])
    return np.array([grad_F1,grad_F2])
print()
print('Jacobiana de F numerica')
print()
print(JF_num(2,1,0).round(1))

def Jg_num(u,v): 
    h=1e-10
    def g1(u,v):  
        return u**2 + v
    def g2(u,v):  
        return np.exp(u)
    def g3(u,v):
        return u*v
    dg1_u = g1(u+h,v)-g1(u,v); dg1_u /=h 
    dg1_v = g1(u,v+h)-g1(u,v); dg1_v /=h
    grad_g1 = np.array([dg1_u,dg1_v])

    dg2_u = g2(u+h,v)-g2(u,v); dg2_u /=h 
    dg2_v = g2(u,v+h)-g2(u,v); dg2_v /=h
    grad_g2 = np.array([dg2_u,dg2_v])

    dg3_u = g3(u+h,v)-g3(u,v); dg3_u /=h 
    dg3_v = g3(u,v+h)-g3(u,v); dg3_v /=h
    grad_g3 = np.array([dg3_u,dg3_v])

    return np.array([grad_g1,grad_g2,grad_g3])
print()
print('Jacobiana de g numerica')
print()
print(Jg_num(0,2).round(1))

def JH_num(u,v):
    g_val=g(u,v)
    return JF_num(g_val[0],g_val[1],g_val[2])@Jg_num(u,v)
print()
print('Jacobiana de H numerica')
print()
print(JH_num(0,2).round(1))






