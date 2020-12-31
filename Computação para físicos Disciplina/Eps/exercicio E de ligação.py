#Erik Kaue  Número usp:8516455
#Calculo de energia de ligação

import numpy as np

a1,a2,a3,a4 = 15.8,18.3,0.714,23.2 #valores das constantes.
M =[]  #Matriz que vai armazenar todos os valores possiveis de B/A usando os possiveis valores de A.
def a5(z,A): #Função para constante a5.
 if A % 2 != 0 :
  return 0
 elif z % 2 == 0 and A % 2 == 0 :
  return 12.0
 elif z % 2 != 0 and A % 2 == 0 :
  return -12.0

for i in range(1,101): #Laço que vai percorrer todos os valores atomicos de Z de 1 até 100.
 B = [] #Lista que vai receber cada valor de B/A.
 for j in range(i,3*i+1): #laço que percorre todos os valor de A entre Z e 3Z.
  B.append((a1*j -a2*j**(2/3) - (a3*i*(i-1))/(j**(1/3)) - (a4*(j-2*i)**(2))/j + a5(i,j)/j**(1/2))/j) #Função de B/A.
 M.append(B)
 print(" O valor de z é:",i,"\n O valor de B/A: ",max(M[i-1]), "\n O valor de A que maximiza B/A: ",M[i-1].index(max(M[i-1])) + i) #index retorna o indice em que o valor está armazenado, nesse caso o valor máximo.


 
  
      
