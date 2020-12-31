from numpy import arange, log10, float32, float64
import matplotlib.pyplot as plt


resultado1 = []
resultado2 = []
P = []
erro1 = []
erro2 = []

def function(x):
 y = 6*(-x**5+1)
 return y

def simpson(a,b,n,f):
 X,Y,I, = [],[],[]
 h = (b-a)/n
 for i in arange(a,b+h,h):
  X.append(i)
  Y.append(f(i))
 for j in range(1,len(Y)-1):
  if j % 2 == 0:  
   I.append(2*Y[j])
  else:
   I.append(4*Y[j])
   
 I.append(Y[0] + Y[j+1])
 soma = float64(sum(I)*(h/3))
 X,Y,I, = [],[],[]
 return soma
 
 
print("\nPRECISÃO SIMPLES\n") 
print("-"*60)
print("|P |  N        |-----Inum---------------|----Erro","-"*20)
print("-"*60)
for p in range(1,26):
 n = 2**p
 resultado1.append(float32(simpson(0,1,n,function)))
 erro1.append(float32(abs(resultado1[p-1] - 5)))
 P.append(p)
 print(f'{p:^2}',f'{"| ":^1}',f'{ n:<8}',f'{"| ":^1}',f'{resultado1[p-1]:^18}',f'{"  |":^1}',f'{erro1[p-1]:>}')
 if abs(5-float32(simpson(0,1,n,function))) != 0.0:
  plt.plot(p,log10(abs(5-float32(simpson(0,1,n,function)))),'g^')
 


print("\nPRECISÃO DUPLA\n")
print("-"*60)
print("|P |  N        |-----Inum---------------|----Erro","-"*20)
print("-"*60)
for p in range(1,26):
 n = 2**p
 resultado2.append(simpson(0,1,n,function))
 erro2.append(float64(abs(resultado1[p-1] - 5)))
 print(f'{p:^2}',f'{"| ":^1}',f'{ n:<8}',f'{"| ":^1}',f'{resultado2[p-1]:^18}',f'{"   |":^1}',f'{abs(5-float64(simpson(0,1,n,function))):>16}')
 if abs(5-float64(simpson(0,1,n,function))) != 0.0:
  plt.plot(p,log10(abs(5-float64(simpson(0,1,n,function)))),'rx')
plt.xlabel("Valores de p")
plt.ylabel("Log(erro) base 10")

plt.show()




