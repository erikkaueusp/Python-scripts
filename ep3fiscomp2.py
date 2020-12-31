#nome: Erik kaue de Oliveira Silva, Nº usp: 8516455
#Fiscomp II - EP3

from numpy import array,arange
import matplotlib.pyplot as plt



#condições iniciais 
b = 0.5 # contatos que cada indivíduo infectado tem por dia
k = 1/14 # fração dos indivíduos infectados cura-se espontaneamente a cada dia
i0 = 10e-6 #infectados iniciais 
r = array([1-i0,0,i0],float) # valores iniciais de suscetíveis,recuperados e infectados 
pontos_r = [] #lista para pontos recuperados
pontos_s = [] #lista para pontos suscetíveis
pontos_i = [] #lista para pontos infectados
t_inicial = 0 
t_final = 100
dt = 0.01
tk = arange(t_inicial,t_final,dt) #lista de intervalo de tempo

#função suscetíveis,recperados e infectados
def f(r,t):
    s0, r0, i0 = r[0], r[1], r[2]
    f0, f1, f2  = -b*s0*i0, k*i0, b*s0*i0 - k*i0
    return array([f0,f1,f2],float)
    
#passo runge kutta 4ª ordem
def passo_rk4(f,r,t,dt):
    k1 = dt*f(r,t)
    k2 = dt*f(r+0.5*k1,t+0.5*dt)
    k3 = dt*f(r+0.5*k2,t+0.5*dt)
    k4 = dt*f(r+k3,t+dt)
    return (k1+2.0*(k2+k3)+k4)/6.0

# integração através do tempo t    
for t in tk:
    pontos_s.append(r[0])
    pontos_r.append(r[1])
    pontos_i.append(r[2])
    r += passo_rk4(f,r,t,dt)



plt.plot(tk,pontos_i,label = "% da população infectada")
plt.plot(tk,pontos_r,label = "% da população recuperada")
plt.plot(tk,pontos_s,label = "% da população suscetível")
plt.xlabel("Dias")
plt.ylabel("% da população ")
plt.title("Modelo SIR")
plt.legend()
plt.grid()
plt.show()
