from math import sin,cos,pi
from numpy import arange, array
import matplotlib.pyplot as plt


def f(r,t):
    x, y = r[0], r[1]
    fx, fy = y, y**2 - x - 5
    return array([fx,fy],float)

def passo_rk2(f,r,t,h):
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    return k2

def passo_lpf(f,r,rpm,t,h):
    r += h*f(rpm,t+0.5*h)
    rpm += h*f(r,t+h)
    return r, rpm

a = 0
b = 50

r_lpf = array([1,0],float)

h = 1e-3
t = 0
rpm = r_lpf + passo_rk2(f,r_lpf,t,h/2)
t_lista = []
x_lista = []
while t<= b:
    t_lista.append(t)
    x_lista.append(r_lpf[0])
    r_lpf, rpm = passo_lpf(f,r_lpf,rpm,t,h)
    t += h
    
plt.plot(t_lista,x_lista)
plt.title("Leapfrog")
plt.xlabel("t")
plt.ylabel("X(t)")
plt.show()
