#Erik Kaue  Número usp:8516455
#Calculo da constante de Madelung

import numpy as np #biblioteca Numpy
import time #Biblioteca time para calcular o tempo de execução

def signeletron(a): #Função que recebe um vetor e devolve 1 se a soma i+j+k for par e -1 se for impar
 if sum(a) % 2 == 0:
  return 1
 else: 
  return -1
def norma(a): #Função que recebe o vetor e retorna o módulo do vetor (i,j,k)
 return np.sqrt(np.dot(a,a))
L = 90 #valor de Lados
m = 0
start_time = time.time() #inicio da execução do tempo do programa
#Combinações de for para percorrer (2l+1)^3 átomos
for k in range(-L,L+1):
 for j in range(-L,L+1):
  for i in range(-L,L+1):
   if (i,j,k) != (0,0,0):
     a = np.array([i,j,k],int)

     m = (signeletron(a)/norma(a)) + m

print("constante M para L=90 é de  ",m)
print("\n\n--- %.5s segundos de execução ---" % (time.time() - start_time)) # tempo final de execução