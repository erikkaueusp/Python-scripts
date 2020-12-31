#nome: Erik kaue de Oliveira Silva, Nº usp: 8516455
#Fiscomp II - EP2

#BLIBIOTECAS UTILIZADAS
from numpy import dot,array
import matplotlib.pyplot as plt
#FUN??O DA EQUA??O GRAVITACIONAL 
def f(r,t):
    G,m1,m2,m3= 1,150,200,250
    rxy1, vxy1 = r[0], r[3] # valores definidos para posi??es -> rxy = [xn,yn] e velocidades -> vxy = [vxn,vyn]
    rxy2, vxy2 = r[1], r[4]
    rxy3, vxy3 = r[2], r[5]
    frxy1, fvxy1 = vxy1 , G*m2*(rxy2-rxy1)/(dot(rxy2-rxy1,rxy2-rxy1)**(1.5)) + G*m3*(rxy3-rxy1)/(dot(rxy3-rxy1,rxy3-rxy1)**(1.5))
    frxy2, fvxy2 = vxy2 , -G*m1*(rxy2-rxy1)/(dot(rxy2-rxy1,rxy2-rxy1)**(1.5)) + G*m3*(rxy3-rxy2)/(dot(rxy3-rxy2,rxy3-rxy2)**(1.5))
    frxy3, fvxy3 = vxy3 , -G*m1*(rxy3-rxy1)/(dot(rxy3-rxy1,rxy3-rxy1)**(1.5)) - G*m2*(rxy3-rxy2)/(dot(rxy3-rxy2,rxy3-rxy2)**(1.5))
    return array([frxy1,frxy2,frxy3,fvxy1,fvxy2,fvxy3],float) # saida para os vetores  posi??es 1,2,3 e velocidades 1,2,3 respectivamente 
    
# m?todo de runge-kutta 4? Ordem
def passo_rk4(f,r,t,h):
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    return (k1+2.0*(k2+k3)+k4)/6.0

#M?todo do passo adaptativo para runge-kutta 4? Ordem
    
def passo_adaptativo(f,r,t,h,prec):
    razao = 1.0 + 1e-10
    while razao >= 1.0 + 1e-10:
        h /= razao
        dr21 = passo_rk4(f,r,t,h)
        dr2 = dr21 + passo_rk4(f,r+dr21,t+h,h)
        dr1 = passo_rk4(f,r,t,2*h)
        epsilon = (dr2 - dr1)/30
        erro = abs(max(epsilon[0][0],epsilon[0][1],epsilon[1][0],epsilon[1][1],epsilon[2][0],epsilon[2][1])) #sendo o erro escolhido atrav?s do maior epsilon de Ex e Ey 1,2,3 tomando seu valor absoluto
        razao = (erro/(h*prec))**0.25
    h_prox = min(h/(razao+1e-10),2*h)
    return dr21, h, h_prox

#CONDI??ES INICIAIS 

r = array([[3,1],[-1,-2],[-1,1],[0,0],[0,0],[0,0]],float) #array definido como o vetor posi??o [x,y] para as estrelas 1,2,3 e suas velocidades [vx,vy] que s?o 0 j? que est?o em repouso.
t_inicial = 0
t_final = 2
h = 0.01 
prec = 1e-5
t = t_inicial
T_list = []
Rx1_list = []
Rx2_list = []
Rx3_list = []
Ry1_list = []
Ry2_list = []
Ry3_list = []
while t <= t_final:
    T_list.append(t)
    Rx1_list.append(r[0][0])
    Ry1_list.append(r[0][1])
    Rx2_list.append(r[1][0])
    Ry2_list.append(r[1][1])
    Rx3_list.append(r[2][0])
    Ry3_list.append(r[2][1])
    dr, h_atual, h_prox = passo_adaptativo(f,r,t,h,prec)
    t, r = t + h_atual, r + dr
    h = h_prox
    
plt.plot(Rx1_list,Ry1_list,label="Estrela 1")
plt.plot(Rx2_list,Ry2_list,label="Estrela 2")
plt.plot(Rx3_list,Ry3_list,label="Estrela 3")
plt.legend()
plt.title("Trajeto das estrelas x por y")
plt.xlabel("x(t)")
plt.ylabel("y(t)")
plt.show()