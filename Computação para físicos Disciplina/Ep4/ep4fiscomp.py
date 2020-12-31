from numpy import tan,sqrt,arange,diff,nan
from matplotlib.pyplot import *


m = 9.1094e-31
h = 1.05457168e-34
w = (1e-9)

def pot1(E):
 return tan(sqrt((w**2*m*E*1.6022e-19)/(2*h**2)))
 
def pot2(E):
 v = 40
 return -sqrt(E/(v-E))

def pot3(E):
 v = 40
 return sqrt((v-E)/E)


dx = 0.001
E = arange(0,20+dx,dx)
P = pot1(E)
P[:-1][diff(P) < 0] = nan


plot(E,P,color='r',label = "Tangente")
plot(E,pot2(E),color='g', label = "Impar")
plot(E,pot3(E),color='b',label = "Par")
ylim(-13,13)
xlim(0,20)
legend()
grid(True)
ylabel("F(E)")
xlabel("E - (eV)")
title("Valores de E para w = 1nm, v = 40eV")
show()

