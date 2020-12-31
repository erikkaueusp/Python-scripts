#metodos comp 2 - Q1
from numpy import arange, exp, cos, sin, log,reshape
import matplotlib.pyplot as plt


#from sklearn.linear_model import LinearRegression

#modelo = LinearRegression()
# Derivada da função 

def f_derivada(t,gama):
    return -2*exp(-gama*t)*(gama*cos(t) + sin(t))

# Função exata
 
def f_exato(t,gama):
    return -2 + 2*exp(-gama*t)*cos(t)




#Método de Euler

#condições iniciais t = 0, x = 0 gama = 1, h = (10-0)/N

gama = 1
N = [8,16,32,64,128,256,512,1024]
X_euler = []
T = []
Lista_de_X_exato = []
erro = []
for n in N:
    x = 0.0
    T1 = []
    X1_euler = []
    X_exato = []
    erro1 = []
    h = 10/n
 
    for t in arange(0,10,h):
     X_exato.append(f_exato(t,gama))
     X1_euler.append(x)
     erro1.append(abs(f_exato(t,gama) - x))
     x += h*f_derivada(t,gama)
     T1.append(t)

    X_euler.append(X1_euler)
    T.append(T1)
    Lista_de_X_exato.append(X_exato)
    erro.append(erro1)

erro_euler = []

for i in range(len(erro)):
    erro_euler.append(sum(erro[i])/len(erro[i]))


#Método de Runge-Kutta

i = 0    
X_rkutta = []
erro_k = []
for n in N:
    x = 0.0
    X1_rkutta = []
    h = 10/n
    erro1_k = []
    for t in T[i]:
     X1_rkutta.append(x)
     erro1_k.append(abs(f_exato(t,gama) - x))
     k2 = h*f_derivada(t+0.5*h,gama)
     x+= k2
     
    X_rkutta.append(X1_rkutta)
    erro_k.append(erro1_k)
    i += 1
    
erro_kutta =[]

for i in range(len(erro_k)):
    erro_kutta.append(sum(erro_k[i])/len(erro_k[i]))
    

plt.scatter(log(N),log(erro_euler),label = "Método de Euler")
plt.scatter(log(N),log(erro_kutta),label = "Método de R.K")
plt.legend()
plt.grid(True)
plt.title("Log(N) x Log(erros) para gama = {}".format(gama))
plt.xlabel("log(N)")
plt.ylabel("Log(erro)")
plt.show()

#A = reshape(log(N),(-1,1))
#B = reshape(log(erro_euler),(-1,1))

#modelo.fit(A,B)
# Não houve alteração na linearidade para valores diferentes de gama.