from math import exp,sqrt
from random import random

# Parâmetros de integração
N = 10**5       # Número de pontos a utilizar para a integração

# Definição da função cujo valor médio será calculado.
# Note que aqui se trata da função de integração dividida por w(x)=x**(-1/2)
def f(x):
    return 1/(x**(1/2)*(1-x)**(1/3))

print("O valor exato da integral entre x=0 e x=1 é",2.58711)
print("")

# Laço de integração pelo método do valor médio
# com amostragem por importância
fsw_medio = 0.0
intw = 1.0  # Integral de w(x)=x**(-1/2) entre x=0 e x=1
for n in range(1,N+1):
    x = random()**2   # Sorteamos a coordenada x do ponto não uniformemente
    fsw_medio += f(x)
fsw_medio /= N
integral = fsw_medio*intw   # Estimativa para a integral
print("A estimativa para a integral pelo método do valor médio é ",integral)
print("")


