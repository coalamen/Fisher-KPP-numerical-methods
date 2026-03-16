import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

## Projet 14 semi-implicite


# Paramètres
J=300
N=400
L=40
T=25

X=np.linspace(-L,L,J+1)
time=np.linspace(0,T,N+1)


#Condition initiale

def u(x):
    return np.sin(x)*[x>0]*[x<np.pi]


#Schéma semi-implicite : Crank-Nicolson

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
ani=anim.FuncAnimation(fig, runanimate, frames=np.arange(N+1), interval=1 , repeat=True )
plt.show()