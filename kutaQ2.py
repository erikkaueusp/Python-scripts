from numpy import arctanh, arange, tanh, float64,inf
import matplotlib.pyplot as plt

def g(x,u):
 t = arctanh(u)
 f = 1/(x**2+t**2)
 return f/(1-u**2)
 
def passo_rk4(f,x,t,h):
 k1 = h*f(x,t)
 k2 = h*f(x+0.5*k1,t+0.5*h)
 k3 = h*f(x+0.5*k2,t+0.5*h)
 k4 = h*f(x+0.5*k3,t+h)
 return (k1+2*(k2+k3)+k4)/6

a = tanh(0)
b = tanh(inf) -1.0e-11
N = 100
h = (b-a)/N
x0 = 1.
xrk4 = x0
u_rk4 = arange(a,b,h)
t_rk4 = []
x_rk4 = []

for u in u_rk4:
 t = arctanh(u)
 t_rk4.append(t)
 x_rk4.append(xrk4)
 xrk4 += passo_rk4(g,xrk4,u,h)
 
plt.plot(t_rk4,x_rk4,)
plt.xlim(0,8)
plt.grid()
plt.show()