from gaussxw import gaussxwab
from numpy import cos,sin,pi,linspace
from matplotlib.pyplot import *
a = 0
b = pi
n = 100
RES1 = []
RES2 = []
X = linspace(0,20,100)

def f(theta,m,x):
 y = cos(m*(theta) - x*sin(theta))/pi
 return y


def simp(a,b,n):
 h = (b-a)/n
 I1 = []
 resultado = []
 for m in range(3):
  for x in X:
   I1.append(float(f(a,m,x)+f(b,m,x)))
   for i in range(1,n):
    if i % 2 == 0:
     I1.append(float((f(a+i*h,m,x)*2)))
    else:
     I1.append(float((f(a+i*h,m,x)*4)))
   
   resultado.append(float(sum(I1)*(h/3)))
   I1 = []
  RES1.append(resultado)
  resultado =[]
   

def quad(a,b,n):
 I2 = []
 resultado = []
 theta,w = gaussxwab(n,a,b)
 for m in range(3):
  for x in X:
   for i in range(n):
    I2.append(float(w[i]*f(theta[i],m,x)))
   resultado.append(float(sum(I2)))
   I2 = []
  RES2.append(resultado)
  resultado = []
   

  

simp(a,b,n)

plot(X,RES1[0],color='r',linestyle = '-',label = 'Jsimp 1')
plot(X,RES1[1],color='g',linestyle = '-',label = 'Jsimp 2')
plot(X,RES1[2],color='b',linestyle = '-',label = 'Jsimp 3')

quad(a,b,n)

plot(X,RES2[0],color='silver',linestyle = '--',label = 'Jquad 1')
plot(X,RES2[1],color='gray',linestyle = '--',label = 'Jquad 2')
plot(X,RES2[2],color='black',linestyle = '--',label = 'Jquad 3')
legend()
grid(True)
ylabel("$J_m(X)$ - Funções de Bessel")
xlabel("x - valores")
show()


