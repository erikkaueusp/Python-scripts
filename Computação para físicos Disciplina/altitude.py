from numpy import loadtxt
from pylab import *

def dev(x):
 h = 0.00000001
 y = f(x+h) - f(x-h)/2*h
 return y
 
batimento = loadtxt("batimento.txt",float)
ruido  = loadtxt("noise.txt",float)




subplot(2,1,1)
plot(batimento[:,0],batimento[:,1])
subplot(2,1,2)
plot(ruido[:,0],ruido[:,1],color = 'black')
show()