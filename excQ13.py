# Questão 1 - Lotka-Volterra

from numpy import array,arange
import matplotlib.pyplot as plt

def f(r,t):
    a,b,c,d = 1,0.5,0.5,2
    x, y = r[0], r[1]
    fx, fy = a*x - b*x*y, c*x*y - d*y
    return array([fx,fy],float)

def passo_rk4(f,x,t,h):
    k1 = h*f(x,t)
    k2 = h*f(x+0.5*k1,t+0.5*h)
    k3 = h*f(x+0.5*k2,t+0.5*h)
    k4 = h*f(x+0.5*k3,t+h)
    return (k1+2*(k2+k3)+k4)/6

#condições iniciais

r = array([2,2],float)
t_inicial = 0
t_final = 30
dt = 0.001
tk = arange(t_inicial,t_final,dt)
points_x = []
points_y = []
for t in tk:
    points_x.append(r[0])
    points_y.append(r[1])
    r += passo_rk4(f,r,t,dt)
    
plt.plot(tk,points_x,c='b',label = 'x(t)')
plt.plot(tk,points_y,c='r',label = 'y(t)')
plt.title("Modelo de presa e predador - (Lotka-Volterra)")
plt.xlabel("t")
plt.ylabel("x(t), y(t)")
plt.legend()
plt.grid()
plt.show()