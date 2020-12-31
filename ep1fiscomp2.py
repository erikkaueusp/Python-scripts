#nome: Erik kaue de Oliveira Silva, Nº usp: 8516455
#Fiscomp II - EP1

from numpy import arange
import matplotlib.pyplot as plt

# Função de onda quadrada
def f(x,t):
 if int(2*t) % 2 == 0 :
  return (1-x)
 else:
  return (-1-x)


# Passo runge-kutta 4
def passo_rk4(f,x,t,h):
 k1 = h*f(x,t)
 k2 = h*f(x+0.5*k1,t+0.5*h)
 k3 = h*f(x+0.5*k2,t+0.5*h)
 k4 = h*f(x+0.5*k3,t+h)
 return (k1+2*(k2+k3)+k4)/6


#condições iniciais

t_inicial = 0.
t_final  = 10.
N = 1000
h = (t_final - t_inicial)/N
V =[]
RC = [0.01,0.1,1]
T = arange(t_inicial,t_final,h)

#gerando gráfico para cada valor de RC

for rc in RC:

 V_out = []
 v_out = 0
 
 for t in T:
  V_out.append(v_out)
  v_out += passo_rk4(f,v_out,t,h)/rc
  
 V.append(V_out)
 

plt.plot(T,V[0],label = "RC = {}".format(RC[0]))
plt.plot(T,V[1],label = "RC = {}".format(RC[1]))
plt.plot(T,V[2],label = "RC = {}".format(RC[2]))
plt.xlabel("T(s)")
plt.ylabel("Vout(V)")
plt.title("Solução Numérica de Vout")
plt.legend()
plt.grid()
plt.show()