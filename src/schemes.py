import numpy as np
import matplotlib.pyplot as plt


## Projet 14


# Paramètres
J=50
L=5
T=1
N=45

X=np.linspace(-L,L,J+1)
time=np.linspace(0,T,N+1)


#Condition initiale

def u(x):
    return np.sin(x)*[x>0]*[x<np.pi]


#Schéma explicite

def schéma_explicite(J,L,T,N,u):
    dt=T/N
    dx=2*L/J
    a=dt/(dx**2)
    
    B=2*np.diag(np.ones(J-1))-np.diag(np.ones(J-2),1)-np.diag(np.ones(J-2),-1)
    A=np.eye(J-1)-a*B
    C=np.zeros(J-1)
    
    v=np.zeros((N+1,J+1))
    v[0]=u(X)
    for n in range(0,N):
        C=v[n,1:-1]*(1-v[n,1:-1])
        v[n+1,1:-1]=np.dot(A,v[n,1:-1])+dt*C
    
    
    for n in range(4,15):
        plt.plot(X,v[n], label=f't={n}')
    plt.legend()
    plt.show()


#Schéma semi-implicite : Crank-Nicolson

def schéma_CN(J,L,T,N,u):
    dt=T/N
    dx=2*L/J
    a=dt/(2*dx**2)
    b=1+2*a
    c=1-2*a
    
    A=b*np.diag(np.ones(J-1))-a*np.diag(np.ones(J-2),1)-a*np.diag(np.ones(J-2),-1)
    B=c*np.diag(np.ones(J-1))+a*np.diag(np.ones(J-2),1)+a*np.diag(np.ones(J-2),-1)
    
    v=np.zeros((N+1,J+1))
    v[0]=u(X)
    for n in range(0,N):
        C=v[n,1:-1]*(1-v[n,1:-1])
        v[n+1,1:-1]=np.linalg.solve(A,np.dot(B,v[n,1:-1])+dt*C)
    
    for n in range(1,6):
        plt.plot(X,v[100*n], label=f't={100*n}')
    plt.legend()
    plt.show()

plt.close()
schéma_explicite(J, L, T, N, u)
























