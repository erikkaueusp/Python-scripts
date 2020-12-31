#metodos comp 2 - Q1-2
from numpy import arange, exp, cos, sin, log10,sqrt
import matplotlib.pyplot as plt


#
# Derivada da função 

def f_derivada(t,gama,omega):
    return -2*exp(-gama*t)*(gama*cos(omega*t) + omega*sin(omega*t))

# Função exata
 
def f_exato(t,gama,omega):
    return -2 + 2*exp(-gama*t)*cos(omega*t)


#Método de Runge-Kutta 4ª ordem

#condições iniciais t = 0, x = 0 gama = 1, h = (10-0)/n, n = 100

OMEGA = [2**j for j in range(0,9)]
gama = 1
n = 100    
X_rkutta = []
erro_k = []
for omega in OMEGA:
    x = 0.0
    X1_rkutta = []
    h = 10/n
    erro1_k = []
    for t in arange(0,10,h):
     X1_rkutta.append(x)
     erro1_k.append(abs(f_exato(t,gama,omega) - x))
     k1 = h*f_derivada(t,gama,omega)
     k2 = h*f_derivada(t+0.5*h,gama,omega)
     k3 = h*f_derivada(t+0.5*h,gama,omega)
     k4 = h*f_derivada(t+h,gama,omega)
     x+= (k1+2*(k2+k3)+k4)/6
     
    X_rkutta.append(X1_rkutta)
    erro_k.append(erro1_k)
    
erro_kutta =[]

for i in range(len(erro_k)):
    erro_kutta.append(sum(erro_k[i])/sqrt(len(erro_k[i])))
    


plt.scatter(log10(OMEGA),log10(erro_kutta),label = "Método de R.K")
plt.legend()
plt.grid(True)
plt.title("Log(N) x Log(erros) para gama = {}".format(gama))
plt.xlabel("log(N)")
plt.ylabel("Log(erro)")
plt.show()


