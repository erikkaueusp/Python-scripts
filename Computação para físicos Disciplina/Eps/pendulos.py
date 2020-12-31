from vpython import *
from numpy import sin,cos,arange,pi,sqrt,empty,array,full
from random import randint
# Controle de camera, para que a camera olhe a parte de trás do pendulo.
quadro = canvas(title='Pendulos',
     width=400, height=300,
     background=color.blue)

quadro.camera.pos = vector(0,0,-16)
quadro.camera.axis = vector(0,-1,10)
# valor n para número de pendulos, g para gravidade, L comprimento dos cabos com uma variação delta(l), t para o tempo inicial e dt variando o tempo de 0.01 e demais vetores representando parametros de velocidade ângular, aceleração, ângulo inicial e coordenadas.
n = 15
g = 9.8
L = array(arange(8.93,8+n,0.4),float)
t = 0
dt = 0.01
w = full((n),0,float)
theta = full((n),0.40,float)
acelera = full((n),0,float)
x = full((n),0,float)
y = full((n),0,float)


stick = cylinder(pos=vector(0,0,0),color = vector(150,75,0), axis = vector(0,0,n),radius = 0.1)
bolas = empty(n,sphere)  #vetor vazio do tipo objeto para armazenar as esferas e os cilindros, nota que o vetor precisa ser vazio caso contrario resultaria numa imagem estatica desses objetos 
cabos = empty(n,cylinder) 


# gerador de números inteiros aleatórios para criar a cor para 'n' pendulos sendo o padrão rgb (red,green,blue) de cores 
for i in range(n):
 r = randint(0,n)
 g = randint(0,n)
 b = randint(0,n)
# objetos que compõe as bolinhas e os cabos que "seguram" as bolinhas
 bolas[i] = sphere(pos = vector(0,0.5-L[i],i), radius = 0.5)
 bolas[i].color = vector(r*0.60,g*0.30,b*0.10)
 cabos[i] = cylinder(pos=vector(0,0,i),axis=vector(0,-L[i],0), radius=0.04 )
 
 

while True: #repetição da animação com os valores deduzios da equação horaria do pendulo para baixas oscilações 
 rate(300)
 
 for i in range(n):
  acelera[i] = -g/L[i]*(sin(theta[i]))
  w[i] = w[i] + acelera[i]*dt
  theta[i] = theta[i] + w[i]*dt
  x[i] = -sin(-theta[i])
  y[i] = -cos(-theta[i])
 
  cabos[i].axis = L[i]*vector(x[i],y[i],0)
  bolas[i].pos = vector(L[i]*x[i],L[i]*y[i],i)
 
  
 t = t + dt
 
 
 
  
  
