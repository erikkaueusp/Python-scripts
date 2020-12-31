#nome: Erik kaue de Oliveira Silva, Nº usp: 8516455
#Fiscomp II - EP3

from numpy import array,arange
import matplotlib.pyplot as plt
import sys

#condições iniciais 
b_inicial = 0.5
b_acima = 0.084 #chute acima para o pico acima do sistema de saúde
b_abaixo = 0.07 #chute abaixo
k = 1/14 # fração dos indivíduos infectados cura-se espontaneamente a cada dia
i0 = 10e-6 #infectados iniciais 
lim_saude = 4e-4 #limite do sistema de saúde
lim_atend = 5e-2 #limite de infectados que precisam de atendimento

ponto_i = []
#points_s = []
#points_i = []
t_inicial = 0
t_final = 1800
dt = 0.01
tk = arange(t_inicial,t_final,dt)
prec = 1e-10

def f(r,t,b):
    s0, r0, i0 = r[0], r[1], r[2]
    f0, f1, f2  = -b*s0*i0, k*i0, b*s0*i0 - k*i0
    return array([f0,f1,f2],float)
    

def passo_rk4(f,r,t,dt,b):
    k1 = dt*f(r,t,b)
    k2 = dt*f(r+0.5*k1,t+0.5*dt,b)
    k3 = dt*f(r+0.5*k2,t+0.5*dt,b)
    k4 = dt*f(r+k3,t+dt,b)
    return (k1+2.0*(k2+k3)+k4)/6.0

# função que retorna o valor do pico para o máximo de infectados que precisam de atendimento hospitalar
def pico(b):
    pontos_s = []
    pontos_r = []
    pontos_i = []
    r = array([1-i0,0,i0],float)
    for t in tk:
        pontos_s.append(r[0])
        pontos_r.append(r[1])
        pontos_i.append(r[2]*lim_atend)
        r += passo_rk4(f,r,t,dt,b)
    return max(pontos_i),pontos_s,pontos_r,pontos_i    

# calculo inicial da diferença entre o tamanho do pico e o limite do sistema de saúde
dif1 = pico(b_acima)[0] - lim_saude
dif2 = pico(b_abaixo)[0] - lim_saude

if (dif1*dif2 > 0):
    sys.exit("Alturas relativas com mesmo sinal. Modifique velocidades.") 

# método da bissecção para retornar o melhor valor de b a ser utilizado.

while (abs(b_acima - b_abaixo) ) > prec:

    bm = (b_acima+b_abaixo)/2
    dif_m = pico(bm)[0] - lim_saude
    if (dif1*dif_m)> 0:
        b_acima, dif1 = bm, dif_m
    else:
        b_abaixo, dif2 = bm, dif_m
            
b = (b_acima+b_abaixo)/2


print("Valor de b é de: ",round(b,3))
print('Fração máxima de pessoas hospitazadas com isolamento {}, sem isolamento {}'.format(pico(b)[0],pico(b_inicial)[0]))


    
plt.axhline(lim_saude,label = "Limite do sistema de saúde",color = 'red')
plt.plot(tk,pico(b)[3],label = "com isolamento, b = {}".format(round(b,3)))
plt.plot(tk,pico(b_inicial)[3],label = "sem isolamento, b = {}".format(b_inicial))
plt.xlabel("Dias")
plt.ylabel("% da população ")
plt.title("Modelo SIR")
plt.legend()
plt.grid()
plt.show()