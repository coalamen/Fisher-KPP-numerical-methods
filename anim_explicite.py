import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

## Projet 14 explicite


# Paramètres
J=500
L=50
T=10
N=600

X=np.linspace(-L,L,J+1)
time=np.linspace(0,T,N+1)


#Condition initiale

def u(x):
    return np.sin(x)*[x>0]*[x<np.pi]


#Schéma explicite

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


#Animation

#Initialisation
Y0=v[0]
fig=plt.figure(1)
plt.clf()
ax=fig.gca()
line1,=ax.plot(X,Y0)
ax.axis([-L,L,-0.1,1.1])

#Màj de chaque plot
def runanimate(n):
    t=n*dt
    line1.set_data(X,v[n])
    ax.set_title(f"Solution approchée à l'instant t^{n}")

#Lancement de l'animation
ani=anim.FuncAnimation(fig, runanimate, frames=np.arange(N+1), interval=0.01 , repeat=True )
plt.show()