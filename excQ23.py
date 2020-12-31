# Questão 2 - Equações de Lorenz

from numpy import array,arange
import matplotlib.pyplot as plt

def f(r,t):
    a,b,c = 10,28,8/3
    x, y, z = r[0], r[1], r[2]
    fx, fy, fz = a*(y-x) ,b*x - y - x*z, x*y -c*z
    return array([fx,fy,fz],float)

def passo_rk4(f,x,t,h):
    k1 = h*f(x,t)
    k2 = h*f(x+0.5*k1,t+0.5*h)
    k3 = h*f(x+0.5*k2,t+0.5*h)
    k4 = h*f(x+0.5*k3,t+h)
    return (k1+2*(k2+k3)+k4)/6

#condições iniciais

r = array([0,1,0],float)
t_inicial = 0
t_final = 50
dt = 0.001
tk = arange(t_inicial,t_final,dt)
points_x = []
points_y = []
points_z = []
for t in tk:
    points_x.append(r[0])
    points_y.append(r[1])
    points_z.append(r[2])
    r += passo_rk4(f,r,t,dt)
    
plt.plot(points_x,points_z,c='b',label = 'z(t)')
plt.title("Atrator")
plt.xlabel("x(t)")
plt.ylabel("z(t)")
plt.figure()
plt.plot(tk,points_y,c='r',label = 'y(t)')
plt.xlabel("t")
plt.ylabel("y(t)")
plt.grid()
plt.legend()
plt.show()