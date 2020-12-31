# Questão 3 - Oscilador Harmonico 

from numpy import array,arange
import matplotlib.pyplot as plt

def f(r,t,w):
    x, y = r[0], r[1]
    fx, fy = y, -w**2*x
    return array([fx,fy],float)

def g(r,t,w):
    x, y = r[0], r[1]
    fx, fy = y, -w**3*x
    return array([fx,fy],float)

def van(r,t,mi):
    w = 1
    x, y = r[0], r[1]
    fx, fy = y, mi*(1-x**2)*y -w**2*x
    return array([fx,fy],float)

def passo_rk4(f,x,t,h,w):
    k1 = h*f(x,t,w)
    k2 = h*f(x+0.5*k1,t+0.5*h,w)
    k3 = h*f(x+0.5*k2,t+0.5*h,w)
    k4 = h*f(x+0.5*k3,t+h,w)
    return (k1+2*(k2+k3)+k4)/6

#condições iniciais

r = array([1,0],float)
s = array([1,0],float)
w = 1
t_inicial = 0
t_final = 20
dt = 0.001
tk = arange(t_inicial,t_final,dt)
fpoint_x = []
fpoint_y = []
gpoint_x = []
gpoint_y = []
for r[0] in range(1,3):
    fX = []
    fY = []
    gX = []
    gY = []
    s[0] = r[0]
    s[1],r[1] = 0,0
    for t in tk:
        fX.append(r[0])
        fY.append(r[1])
        gX.append(s[0])
        gY.append(s[1])
        s += passo_rk4(g,s,t,dt,w)
        r += passo_rk4(f,r,t,dt,w)
    fpoint_x.append(fX)
    fpoint_y.append(fY)
    gpoint_x.append(gX)
    gpoint_y.append(gY)

plt.plot(tk,fpoint_x[0],c='b',label="x = {}".format(fpoint_x[0][0]))
plt.plot(tk,fpoint_x[1],c='r',label="x = {}".format(fpoint_x[1][0]))
plt.title("Oscilador Harmonico Simples")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.legend()
plt.grid()
plt.figure()
plt.plot(tk,gpoint_x[0],c='b',label="x = {}".format(gpoint_x[0][0]))
plt.plot(tk,gpoint_x[1],c='r',label="x = {}".format(gpoint_x[1][0]))
plt.title("Oscilador Cúbico")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.legend()
plt.grid()
plt.figure()
plt.plot(fpoint_x[0],fpoint_y[0],c='b',label="x = {}".format(fpoint_x[0][0]))
plt.plot(fpoint_x[1],fpoint_y[1],c='r',label="x = {}".format(fpoint_x[1][0]))
plt.title("Oscilador Harmonico Simples(Espaço de Fase")
plt.xlabel("v(t)")
plt.ylabel("x(t)")
plt.figure()
plt.plot(gpoint_x[0],gpoint_y[0],c='b',label="x = {}".format(gpoint_x[0][0]))
plt.plot(gpoint_x[1],gpoint_y[1],c='r',label="x = {}".format(gpoint_x[1][0]))
plt.title("Oscilador Cúbico(Espaço de Fase)")
plt.xlabel("v(t)")
plt.ylabel("x(t)")


#Oscilador de van der Pol.

#condições iniciais


Velocidades = []
X_valores = []
MI = [1,2,4]
for mi in MI:
    r = array([1,0],float)
    V = []
    X = []
    for t in tk:
        X.append(r[0])
        V.append(r[1])
        r += passo_rk4(van,r,t,dt,mi)
    X_valores.append(X)
    Velocidades.append(V)
    
plt.figure()
plt.plot(X_valores[0],Velocidades[0],label="$\mu$ = {}".format(MI[0]))
plt.plot(X_valores[1],Velocidades[1],label="$\mu$ = {}".format(MI[1]))
plt.plot(X_valores[2],Velocidades[2],label="$\mu$ = {}".format(MI[2]))
plt.xlabel("x(t)")
plt.ylabel("V(t)")
plt.title("Oscilador de van der Pol")
plt.legend()
plt.show()
        