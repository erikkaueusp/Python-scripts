#nome Erik Kaue de Oliveira Silva nº usp: 8516455
#Ep 4

from random import randrange
from numpy import array,zeros
import matplotlib.pyplot as plt

# Constantes
L = 200     # L+1, com L par, é o lado da rede quadrada

# Criando listas para armazenar a trajetória
data = zeros((L+1,L+1),dtype=int)



# A partícula sai da origem
x, y = 0, 0

while data[int(L/2)][int(L/2)] != 1:

    z = randrange(4)   # Sorteamos uma de quatro direções
    if z == 0:
        dr = [1,0]  # Passo para a direita
    if z == 1:
        dr = [0,1]  # Passo para cima
    if z == 2:
        dr = [-1,0] # Passo para a esquerda
    if z == 3:
        dr = [0,-1] # Passo para baixo

        
    # Não permitimos que a partícula saia da rede
    if (abs(x+dr[0])<=L/2) and (abs(y+dr[1])<=L/2):
        x += dr[0]
        y += dr[1]
        if data[int(x+L/2)][int(y+L/2)] != 1 :
            if (abs(x) == L/2 or abs(y) == L/2 ):
            #condição para que a particula grude se caso estiver proximo as laterais    
                data[int(x+L/2)][int(y+L/2)] = 1
                x,y = 0,0
            # Condição para que a particula seja registrada num sitio próximo de outra particula     
            elif (data[int(x-1+L/2)][int(y+L/2)] == 1 or data[int(x+1+L/2)][int(y+L/2)] == 1
                 or data[int(x+1+L/2)][int(y+1+L/2)] == 1 or data[int(x+L/2)][int(y+1+L/2)] == 1 
                 or data[int(x+L/2)][int(y-1+L/2)] == 1 or data[int(x+1+L/2)][int(y-1+L/2)] == 1):
                 
                data[int(x+L/2)][int(y+L/2)] = 1
                x,y = 0,0
                
    


plt.title("Agregação limitada por difusão")
plt.xlabel("eixo x")
plt.ylabel("eixo y")
plt.imshow(data,extent=[-L/2,L/2,-L/2,L/2],cmap = 'YlOrBr',)
plt.show()
            

