#Erik Kaue  Número usp:8516455
#números primos

lista =[2]
def primo(n):
 if( n > 1 ):
  for i in range(2,n): #vai percorrer todos os valores de 2 até n-1
   if ((n % i) == 0): # condicional para o resto da divisão, se não for divisivel por n-1 valores então é primo
    return
  lista.append(n)
for n in range(3,10001):
 primo(n)
print(lista)