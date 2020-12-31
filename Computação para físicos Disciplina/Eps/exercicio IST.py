#Erik Kaue  Número usp:8516455
#Indice de Similaridade com a Terra(IST).

import numpy as np

a = np.loadtxt('dados.txt') # comando para receber valores do arquivo txt no array.
omega = [0.57,1.07,0.7,5.58] #valores de omega para cada constante w1,w2,w3 e w4.
matriz = [] # 12x4 que receberá o resultado de cada produto para cada planeta.
planetas = ['Terra','Marte','Mercúrio','Lua','Vênus','Io','Júpiter','Titã','Gj 581 g','Gj 581 b','HD 96167 b', 'WASP-26 B']
for i in a: #percorre 12 vezes a matriz atribuindo para cada i sua linha.
 ist = [] #recebe o valor dos 4 produtos.
 for j in range(len(i)):
  if j == 3:
   ist.append((1 - abs((i[j] - 288)/(i[j] + 288)))**(omega[j]/4)) # armazena o valor para a temperatura.

  else:
    ist.append((1 - abs((i[j] - 1)/(i[j] + 1)))**(omega[j]/4)) #armazena demais valores dos outros 3 produtos.
 matriz.append(ist) #monta a matriz.

for i in range(12): # percorre a matriz para gerar o produtório e entregar os valores de cada IST para cada planeta.
 IST = 1
 for k in range(4):
  IST = IST*matriz[i][k]
 print("\n O valor para o planeta: %s é de %f" %(planetas[i],IST))
  

   
  
  
  
 
 