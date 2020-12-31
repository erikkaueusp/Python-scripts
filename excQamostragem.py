from math import sqrt
from random import random

# Parâmetros de integração
N = 10**2       # Número de pontos a utilizar para a integração
a = 0.5
b = 1
c = 0
# Definição da função cujo valor médio será calculado.
# Note que aqui se trata da função de integração dividida por w(x)=x**(-1/2)
def f(x):
    return 1/((1-x)**(1/3))

def g(x):
    return 1/(x**(1/2))
print("O valor exato da integral entre x=0 e x=1 é",2.58711)
print("")

# Laço de integração pelo método do valor médio
# com amostragem por importância
fsw_medio1 = 0.0
fsw_medio2 = 0.0
intw1 = sqrt(2.0)  # Integral de w1(x) = x**(-1/2) entre x=0 e x=1/2
intw2 = 3*(2)**(1/3)/4 #Integral de w2(x) = (1-x)**(-3/2) entre x=1/2 e x=1
for n in range(1,N+1):
    x = (c + (a-c)*random())**2/2   # Sorteamos a coordenada x do ponto não uniformemente
    y = (2-(a + (b-a)*random())**(3/2))/2 #Sorteamos a coordenada y do ponto não uniformemente 
    fsw_medio1 += f(x)
    fsw_medio2 += g(y)
fsw_medio1 /= N
fsw_medio2 /= N

integral1 = fsw_medio1*intw1   # Estimativa para a integral1
integral2 = fsw_medio2*intw2   # Estimativa para a integral2

integral = integral1 + integral2
print("A estimativa para a integral pelo método do valor médio é ",integral)
print("")


