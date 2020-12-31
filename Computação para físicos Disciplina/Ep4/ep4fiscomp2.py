from numpy import tan,sqrt, arange,seterr, pi, diff, nan
from matplotlib.pyplot import *

seterr(divide='ignore',invalid='ignore')

m = 9.1094e-31
h = 1.05457168e-34
w = 1e-9

def dif1(E):
 v = 20
 y = tan(sqrt((w**2*m*E*1.6022e-19)/(2*h**2))) + sqrt(E/(v-E))
 return y
 
 
 
 
 
def bin(x1,x2):
 xm = (x1+x2)/2
 while abs(dif(xm)) > 0.001:
  print(xm)
  print(abs((pot1(xm) - pot2(xm))))
  if (pot1(xm) - pot2(xm)) > 0:
   x1 = xm
   xm = (x1+x2)/2
   print("POSITIVO")
  else:
   x2 = xm
   xm = (x1+x2)/2
   print("NEGATIVO")
 return ((pot1(x1) - pot2(x1))),((pot1(x2) - pot2(x2))),x1,x2


def pot1(E):
 m = 9.1094e-31
 h = 1.05457168e-34
 w = 1e-9
 return tan(sqrt((w**2*m*E*1.6022e-19)/(2*h**2)))
 
def pot2(E):
 v = 20
 return -sqrt(E/(v-E))

def pot3(E):
 v = 20
 return sqrt((v-E)/E)


dx = 0.001
E = arange(0,20+dx,dx)
P = pot1(E)
P[:-1][diff(P) < 0] = nan


grid(True)

plot(E,P,color='r',label = "E")
#plot(E,pot2(E),color='g', label = "E impares")
#plot(E,pot3(E),color='b',label = "E pares")
ylim(-15,15)
xlim(0,20)
legend()


show()
