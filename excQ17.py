#Nome: Erik Kaue nºusp: 8516455

from numpy import arange,array
import time
import sys

tempo_inicial = time.time()

# Constantes
g = 9.8       # Aceleração da gravidade
m = 0.4           # Massa da bola
rho = 0.1         # constante de viscosidade
ta = 0.0          # Início do intervalo da variável independente
tb = 3.0         # Final do intervalo da variável independente
ya1 = 40.0          # Palpite inicial para altura acima da desejada
ya2 = 10.0          # Palpite inicial para altura abaixo da desejada
yb = 0.0          # Valor da variável independente no final do intervalo
dt = 1e-2         # Tamanho do passo de integração
prec = 1e-10      # Precisão do resultado para a altura inicial

def f(r,t):
    y, v = r[0], r[1]
    f0, f1 = v, -m*g - rho*v
    return array([f0,f1],float)

def passo_rk4(f,r,t,dt):            # Calcula um passo no método de RK4
    k1 = dt*f(r,t)
    k2 = dt*f(r+0.5*k1,t+0.5*dt)
    k3 = dt*f(r+0.5*k2,t+0.5*dt)
    k4 = dt*f(r+k3,t+dt)
    return (k1+2.0*(k2+k3)+k4)/6.0


def r_final(f,ta,tb,ra,dt):
    r = ra
    for t in arange(ta,tb,dt):
        r += passo_rk4(f,r,t,dt)
    return r

# Solução via método da bissecção (busca binária)
v1 = 0   # Parte do repouso
r1 = array([ya1,v1],float)   # Vetor 'r' inicial correspondente a 'ya1'
r2 = array([ya2,v1],float)   # Vetor 'r' inicial correspondente a 'ya2'
altura1 = r_final(f,ta,tb,r1,dt)[0] - yb # Alt. relativa final partindo com 'ya1'
altura2 = r_final(f,ta,tb,r2,dt)[0] - yb # Alt. relativa final partindo com 'ya2'
if (altura1*altura2 > 0):
    sys.exit("Alturas relativas com mesmo sinal. Modifique as alturas iniciais.")
while abs(ya2-ya1) > prec:
    yp = (ya1+ya2)/2                           # Média entre 'ya1' e 'ya2'
    rp = array([yp,v1],float)                # Vetor 'r' inicial correspondente
    alturap = r_final(f,ta,tb,rp,dt)[0] - yb # Altura relativa correspondente
    if (altura1 * alturap) > 0:              # Altura final menor que desejada?  
        ya1, altura1 = yp, alturap            # Sim; aumentamos o palpite 'ya1'
    else:
        ya2, altura2 = yp, alturap            # Não; diminuímos o palpite 'ya2'
y = (ya1+ya2)/2       # Resultado final do cálculo

print("Tempo de execução (em segundos):",(time.time() - tempo_inicial))
print("A altura inicial necessária é",y,"m")

