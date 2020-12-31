#Nome: Erik Kaue número usp: 8516455
#Exercicio Duplo fatorial (recursão)

def duplofatorial(n): # recursão da função duplo fatorial para valores inteiros de n.
 if n == 1 or n == 0:
  return 1
 else:
  return n*duplofatorial(n-2)
 
for i in range (1,21):
 print("\nO valor de %i fatorial é %i \n" %(i,duplofatorial(i)))