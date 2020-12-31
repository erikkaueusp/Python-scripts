from math import sin,cos,pi
from numpy import arange, array, empty, shape
import matplotlib.pyplot as plt


# Constantes

a = 0       # Início do intervalo de integração
b = 20       # Final do intervalo de integração
prec = 1e-10   # Precisão requerida para o cálculo
H = 20       # Tamanho sugerido do passo de integração
nmax = 8     # Número máximo de iterações do algoritmo de Bulirsch-Stoer

x0, y0 = 0, 0  # Condições iniciais

def f(r,t):
    a,b = 1,3
    x, y = r[0], r[1]
    f0,f1 = 1-(b+1)*x+a*x**2*y,b*x-a*x**2*y
    return array([f0,f1],float)

def passo_mbs_indiv(f,r,t,H,prec,nmax):
    # Calcula um passo no método de Bulirsch-Stoer. Caso se atinjam
    # 'nmax' iterações sem convergência, retorna a informação
    # Inicializamos com um passo do método do ponto médio modificado
    # A matriz R1 armazena a primeira linha da tabela de extrapolação.
    # Por agora, essa linha contém apenas a estimativa do método do
    # ponto médio modificado para a solução no final do intervalo.
    converge = False
    n = 1
    y = r + 0.5*H*f(r,t)
    x = r + H*f(y,t+0.5*H)
    R1 = empty([1,r.shape[0]],float)
    R1[0] = 0.5*(y + x + 0.5*H*f(x,t+H))
    # Agora fazemos um laço aumentando o valor de n até que a precisão
    # seja atingida.
    for n in range(2,nmax+1):
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
        if erro <= H*prec:
            converge = True
            break
        R1 = R2
    # Fazemos r igual à estimativa mais precisa de que dispomos
    r = R2[n-1]
    return converge, r  # Retornamos o NOVO VALOR de r

def passo_mbs_adapt(f,H,prec,nmax,r_lista,t_lista):
    # Calcula um passo no método de Bulirsch-Stoer adaptativo.
    # Esta função não retorna nenhum valor, mas apenas atualiza as listas
    # de t e de r ao atingir convergência em até 'nmax' iterações
    r = r_lista[-1]
    t = t_lista[-1]
    converge, r = passo_mbs_indiv(f,r,t,H,prec,nmax)
    if converge == False: # Se não houve convergência, divida o passo por 2
        passo_mbs_adapt(f,H/2,prec,nmax,r_lista,t_lista)
    else:
        t_lista.append(t+H)
        r_lista.append(r)

def integ_mbs_adapt(f,r_a,a,b,H,prec,nmax,r_lista,t_lista):
    # Esta função percorre o intervalo de integração, determinando os
    # valores de r e t com passo máximo de tamanho H, que é subdividido
    # caso não se atinja a precisão requerida em até 'nmax' iterações
    # do algoritmo de Bulirsch-Stoer. A função não retorna um valor,
    # mas atualiza as listas de r e t.
    t = a
    t_lista.append(t)    # Registramos o valor inicial de t
    r_lista.append(r_a)  # Registramos o valor inicial de r
    while t < b:
        passo_mbs_adapt(f,H,prec,nmax,r_lista,t_lista)
        t = t_lista[-1]  # Atualizamos t para o último valor calculado

# Invocando a integração e criando as listas para traçar os gráficos
r_a = array([x0,y0],float)    # Condição inicial
r_lista, t_lista = [], []
integ_mbs_adapt(f,r_a,a,b,H,prec,nmax,r_lista,t_lista)

X = []
Y = []
h_lista = []
for i in range(len(t_lista)):
    X.append(r_lista[i][0])
    Y.append(r_lista[i][1])
    h_lista.append(t_lista[i]-t_lista[i-1])
h_lista[0] = h_lista[1]




plt.title("Bulirsch-Stoer adaptativo")
plt.xlabel("t")
plt.ylabel("x(t),y(t)")
plt.plot(t_lista,X,label = '[x]')
plt.plot(t_lista,Y,label = '[y]')
plt.legend()
plt.show()

