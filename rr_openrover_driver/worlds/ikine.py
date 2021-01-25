import numpy as np
from copy import copy

cos=np.cos; sin=np.sin; pi=np.pi

def jacobian_ur5(q, delta=0.001):
    """
    Jacobiano analitico para la posicion. Retorna una matriz de 3x6 y toma como
    entrada el vector de configuracion articular q=[q1, q2, q3, q4, q5, q6]

    """
    # Alocacion de memoria
    J = np.zeros((3,7))
    # Transformacion homogenea inicial (usando q)
    Th=fkine_ur5(q)
    aux1=np.array(Th)
    #Th=fkine_ur5([0 0 0 0 0 0])
    # Iteracion para la derivada de cada columna
    for i in xrange(7):
        # Copiar la configuracion articular inicial
        dq = copy(q)
        # Incrementar la articulacion iesima usando un delta
        dq[i]=dq[i]+delta
        # Transformacion homogenea luego del incremento (q+dq)  
        Th_inc=fkine_ur5(dq)
        # Aproximacion del Jacobiano de posicion usando diferencias finitas
        aux2=np.array(Th_inc)
        for k in xrange(3):
            J[k,i]=(aux2[k,3]-aux1[k,3])/delta
    
    

    return J

def dh(d, theta, a, alpha):
    """
    Calcular la matriz de transformacion homogenea asociada con los parametros
    de Denavit-Hartenberg.
    Los valores d, theta, a, alpha son escalares.

    """
    fila1=[cos(theta),-cos(alpha)*sin(theta),sin(alpha)*sin(theta),a*cos(theta)]
    fila2=[sin(theta),cos(alpha)*cos(theta),-sin(alpha)*cos(theta),a*sin(theta)]
    fila3=[0,sin(alpha),cos(alpha),d]
    fila4=[0,0,0,1]
    T = [fila1,fila2,fila3,fila4]
    return T
def fkine_ur5(q):
    """
    Cinematica directa del robot
    """
    # Longitudes (completar)
    L0=0.06
    L1=0.117
    L2=0.352
    L3=0.3215
    L4=0.30495

    # Matrices DH (completar)
    T1 = dh(L0,q[0],L1,-pi/2) 
    T2 = dh(0,q[1]-pi/2,0,-pi/2)
    T3 = dh(L2,q[2],0,pi/2)
    T4 = dh(0,q[3],0,-pi/2)
    T5 = dh(L3,q[4],0,pi/2)
    T6 = dh(0,q[5],0,-pi/2)
    T7 = dh(L4,q[6],0,0)
  
    # Efector final con respecto a la base
    T12 = np.dot(T1,T2)
    T34 = np.dot(T3,T4)
    T56 = np.dot(T5,T6)
    T14 = np.dot(T12,T34)
    T16 = np.dot(T14,T56)
    Ttotal =np.dot(T16,T7)
    return Ttotal

def ikine_ur5(xdes, q0):
    """
    #Calcular la cinematica inversa de UR5 numericamente a partir de la configuracion articular inicial de q0. 
    """
    epsilon  = 0.001
    max_iter = 1000
    delta    = 0.0001

    q  = copy(q0)
    for i in range(max_iter):
        # Main loop
        aux2=np.array(fkine_ur5(q)) #valor de funcion actual
        dif=jacobian_ur5(q,delta)   #primera diferencia 
            
        e=xdes-aux2[0:3,3]
        q=q+np.dot(np.linalg.pinv(dif),e)
     
        if (np.linalg.norm(e) < epsilon):
            break
        
    return q
