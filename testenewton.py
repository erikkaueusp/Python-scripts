from math import sin,cos,pi
from numpy import arange, array, empty, shape
import matplotlib.pyplot as plt


# Constantes

a = 0      # Início do intervalo de integração
b = 20       # Final do intervalo de integração
prec = 1e-10   # Precisão requerida para o cálculo
h = 20       # Tamanho do passo de integração

x0, y0 = 0, 0  # Condições iniciais

def f(r,t):
    a,b = 1,3
    x, y = r[0], r[1]
    f0,f1 = 1-(b+1)*x+a*x**2*y,b*x-a*x**2*y
    return array([f0,f1],float)

def passo_mbs(f,r,t,H,prec): # Calcula um passo no método de Bulirsch-Stoer
    # Inicializamos com um passo do método do ponto médio modificado
    # A matriz R1 armazena a primeira linha da tabela de extrapolação.
    # Por agora, essa linha contém apenas a estimativa do método do
    # ponto médio modificado para a solução no final do intervalo.
    n = 1
    y = r + 0.5*H*f(r,t)
    x = r + H*f(y,t+0.5*H)
    R1 = empty([1,r.shape[0]],float)
    R1[0] = 0.5*(y + x + 0.5*H*f(x,t+H))
    # Agora fazemos um laço aumentando o valor de n até que a precisão
    # seja atingida.
    erro = 2*H*prec # Garantindo que o laço seja executado ao menos 1 vez
    while erro > H*prec:
        n += 1
        h = H/n
        # Método do ponto médio modificado
        y = r + 0.5*h*f(r,t)
        x = r + h*f(y,t+0.5*h)
        for i in range(n-1):
            y += h*f(x,t+(i+1.0)*h)
            x += h*f(y,t+(i+1.5)*h)
        # Calculando as estimativas por extrapolação.
        # As matrizes R1 e R2 armazenam a penúltima e a última
        # linhas mais recentes da tabela
        R2 = empty([n,r.shape[0]],float)
        R2[0] = 0.5*(y + x + 0.5*h*f(x,t+h))
        for m in range(1,n):
            epsilon = (R2[m-1]-R1[m-1])/((n/(n-1))**(2*m)-1)
            R2[m] = R2[m-1] + epsilon
        erro = abs(epsilon[0])
        R1 = R2
    # Fazemos r igual à estimativa mais precisa de que dispomos
    r = R2[n-1]
    #print("t=",t," n='",n) # Imprime o tempo e o n para convergência
    return r        # Retornamos o NOVO VALOR de r

X = []
Y = []
t_lista = []
r_mbs = array([x0,y0],float)
t = 0
while t<= b:   # Realizando a integração numérica
    t_lista.append(t)
    X.append(r_mbs[0])
    Y.append(r_mbs[1])
    r_mbs = passo_mbs(f,r_mbs,t,h,prec)
    t += h
    



plt.title("Bulirsch-Stoer")
plt.xlabel("t")
plt.ylabel("theta(t)")
plt.plot(t_lista,X)
plt.plot(t_lista,Y,"b.")
plt.show()
