from numpy import tan,sqrt

m = 9.1094e-31
h = 1.05457168e-34
w = 1e-9


def busca(x1,x2,func):
 xm = (x1+x2)/2
 while abs(func(xm)) > 0.001:
  xm = (x1+x2)/2
  if func(x1) > 0:
   if func(xm)> 0:
    x1 = xm
   else:
    x2 = xm
  else:
   if func(xm) < 0 :
    x1 = xm
   else:
    x2 = xm
 if min(func(x1),func(x2)) == func(x1):
  return x1
  
 else:
  return func(x2), x2

def difimpar(E):
 v = 20
 y = tan(sqrt((w**2*m*E*1.6022e-19)/(2*h**2))) + sqrt(E/(v-E))
 return y
 
def difpar(E):
 v = 20
 y = tan(sqrt((w**2*m*E*1.6022e-19)/(2*h**2))) - sqrt((v-E)/E)
 return y
 
print("Valor de E0 =",busca(0.3,0.4,difpar))
print("Valor de E1 =",busca(1.25,1.27,difimpar))
print("Valor de E2 =",busca(2.84,2.86,difpar))
print("Valor de E3 =",busca(5,5.2,difimpar))
print("Valor de E4 =",busca(7.5,8,difpar))
print("Valor de E5 =",busca(11.1,11.3,difimpar))
print("Valor de E6 =",busca(15.0,15.1,difpar))
