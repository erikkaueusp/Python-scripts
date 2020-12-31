from math import exp
from random import random,randrange
from numpy import full
import matplotlib.pyplot as plt


# Parâmetros e constantes da simulação
N = 10**4                   # Número de átomos
B = 2 # Campo magnetico 
kB = 1              # Constante de Boltzmann
T = 1           # Temperatura
Passos = 200                # Número de passos de Monte Carlo da simulação
kBT = kB*T

# Matriz que armazena os números quânticos
n = full([1,N],-0.5)        # Partimos do estado fundamental

# Laço principal
E_lista = []                # Lista para armazenar a energia
E = 0
for i in range(N):
    E += n[0,i]
E *= -B
for k in range(Passos):     # Percorremos os passos de Monte Carlo
    # Escolhemos um número quântico que tentaremos alterar
    for l in range(N):          # Cada partícula em média tem 1 chance de mudar 
        i = randrange(N)               # Partícula
        j = randrange(1)               # Número quântico da partícula
        if random() < 0.5:             # Com probabilidade 1/2
            dn = -0.5
            dE = (2*n[j,i])*B  # Variação da energia
        else:                          # Caso contrário1
            dn = 0.5             
            dE = 0
        if random() < exp(-dE/kBT):    # Decidimos se aceitamos a alteração
            n[j,i] = dn
            E += dE
    # Registramos a energia a cada passo de Monte Carlo
    E_lista.append(E/N)        # Energia por partícula (medida em kB*T)
    


plt.plot(E_lista)
plt.title("B = {} ".format(B))
plt.ylabel("m")
plt.xlabel("Passo de Monte Carlo")
plt.show()

