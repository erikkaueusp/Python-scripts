import numpy as np
import matplotlib.pyplot as plt

def func1(x):
 r = 3.7
 x = r*x*(1-x)
 return x
n = int(1/0.01+1)
vetor1 = np.empty([2,n])
vetor2 = np.empty([1,n])
vetor3 = np.empty([2,n])
m = 0
v = 0.73
for i in np.arange(0,1+0.01,0.01):
 vetor1[0,m] = i
 vetor1[1,m] = func1(i)
 vetor2[0,m] = i
 vetor3[0,m] = v
 if m % 2 == 0:
  vetor3[1,m] = func1(v)
  v = func1(v)
 else:
  vetor3[1,m] = v
  
 
 
 m += 1
plt.axhline(0,color='g',lw=0.5)
plt.axvline(0,color = 'g',lw=0.5)
plt.plot(vetor1[0],vetor1[1],color = 'b')
plt.plot(vetor2[0],vetor2[0],color ='r')
plt.plot(vetor3[0],vetor3[1],color = 'black', lw = 0.5)

plt.show()