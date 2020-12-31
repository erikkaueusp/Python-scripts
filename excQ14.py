# Questão 1 - Oscilador harmônico amortecido e forçado

from numpy import array, cos,sin, sqrt, arccos, e
import matplotlib.pyplot as plt

def f(r,t):
    m, k, ro, F, w_ext = 1, 1, 0.4, 1, 0.1 
    x, y = r[0], r[1]
    fx, fy = y ,(-k*x-ro*y+ F*cos(w_ext*t))/m
    return array([fx,fy],float)

def passo_rk4(f,x,t,h):
    k1 = h*f(x,t)
    k2 = h*f(x+0.5*k1,t+0.5*h)
    k3 = h*f(x+0.5*k2,t+0.5*h)
    k4 = h*f(x+0.5*k3,t+h)
    return (k1+2*(k2+k3)+k4)/6


def passo_adaptativo(f,r,t,h,prec):
    razao = 1.0 + 1e-10
    while razao >= 1.0 + 1e-10:
        h /= razao
        dr21 = passo_rk4(f,r,t,h)
        dr2 = dr21 + passo_rk4(f,r+dr21,t+h,h)
        dr1 = passo_rk4(f,r,t,2*h)
        epsilon = (dr2 - dr1)/30
        erro = abs(epsilon[0])
        razao = (erro/(h*prec))**0.25
    h_prox = min(h/(razao+1e-10),2*h)
    return dr21, h, h_prox

def sol_exata(t):
 m, k, w, ro, F = 1 ,1, 0.1, 0.4, 1
 w_0, gama = sqrt(k/m), ro/m
 omega = sqrt(w_0**2 - gama**2/4)
 A_ext = (F/m)/(sqrt((w_0**2 - w**2)**2 + (gama*w)**2))
 phi = -arccos((w_0**2 - w**2)/(sqrt((w_0**2 - w**2) + (gama*w)**2)))
 alpha = 1 - A_ext*cos(phi)
 beta = ((gama*alpha) + 2*w*sin(phi) - 2)/(2*omega)
 return (e**(-gama*t/2)*((alpha)*cos(omega*t) + (beta)*sin(omega*t)) + A_ext*cos(w*t + phi))

#condições iniciais

r = array([0,-1],float)
t_inicial = 0
t_final = 100
h = 0.01
prec = 1e-4
t = t_inicial
T_list = []
V_list = []
X_list = []
X_sol = []
h_valores = []
while t <= t_final:
    h_valores.append(h)
    T_list.append(t)
    V_list.append(r[1])
    X_list.append(r[0])
    X_sol.append(sol_exata(t))
    dr, h_atual, h_prox = passo_adaptativo(f,r,t,h,prec)
    t, r = t + h_atual, r + dr
    h = h_prox

plt.scatter(T_list,X_list,s=8,c='red',label="aproximação")
plt.plot(T_list,X_sol,label="solução")
plt.scatter(T_list,h_valores,s=10,c='green',label="h(t)")
plt.xlabel("t")
plt.ylabel("x(t), h(t)")
plt.legend()
plt.show()