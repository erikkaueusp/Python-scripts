from numpy import exp,cos,sin,arange
import matplotlib.pyplot as plt

def g(x,u):
 gama,omega = 1.0,10.0
 t = u/(1.0-u)
 f = -2.0*exp(-gama*t)*(gama*cos(omega*t)+omega*sin(omega*t))
 return f/(1.0-u)**2
 
def passo_rk4(f,x,t,h):
 k1 = h*f(x,t)
 k2 = h*f(x+0.5*k1,t+0.5*h)
 k3 = h*f(x+0.5*k2,t+0.5*h)
 k4 = h*f(x+0.5*k3,t+h)
 return (k1+2*(k2+k3)+k4)/6

a = 1.e-9
b = 1.0-1.0e-9
N = 200
h = (b-a)/N
x0 = 0.0
xrk4 = x0
u_rk4 = arange(a,b,h)
t_rk4 = []
x_rk4 = []

for u in u_rk4:
 t = u/(1.0-u)
 t_rk4.append(t)
 x_rk4.append(xrk4)
 xrk4 += passo_rk4(g,xrk4,u,h)
 
plt.plot(t_rk4,x_rk4,)
plt.grid()
plt.show()