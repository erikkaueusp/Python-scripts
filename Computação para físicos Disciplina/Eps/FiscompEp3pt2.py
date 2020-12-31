from gaussxw import gaussxwab
from numpy import cos,sin,pi,sqrt,empty,linspace,arange
from pylab import *
a = 0
b = pi
n = 100
comprimento = 1e-3
k1 = float((2*pi)/(400*comprimento))
k2 = float(2*pi/(700*comprimento))
I1 = empty([n,n],float)
I2 = empty([n,n],float)
l = 0
m = 0
  
def f(theta,x):
 y = cos((theta) - x*sin(theta))/pi
 return y

def quad(a,b,n,x):
 Integral = []
 theta,w = gaussxwab(n,a,b)
 for i in range(n):
  Integral.append(float(w[i]*f(theta[i],x)))
 return float(sum(Integral))
  
for x in linspace(-1,1,n):
 m = 0
 for y in linspace(-1,1,n):
  r = sqrt(x**2 + y**2)
  I1[l,m] = float((quad(a,b,10,k1*r)/(k1*r))**2)
  I2[l,m] = (quad(a,b,n,k2)/(k2*r))**2
  m+=1
 l+=1

imshow(I1,extent = [-1,1,-1,1])

hot()
show()
  
