from random import random
from math import sqrt

def f(x):
    result = 1/(x**(1/2)*(1-x)**(1/3))
    return result

#condições iniciais

a = 0
b = 1
h = 5
N = 10**6
k = 0

for n in range(N):
    
    x = a + (b-a)*random()
    y = h*random()
    if y < f(x):
        k += 1
        
integral = k/N*(b-a)*h

print(integral)
        
    