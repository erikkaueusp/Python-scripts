from gaussxw import gaussxwab
from matplotlib.font_manager import FontProperties
from matplotlib.pyplot import *
from numpy import arange
a = 0
b = 2

def f(x):
 y = x**4 -2*x + 1
 return y
def ret(a,b,f,n):
 h = (b-a)/n
 integral = []
 
 for i in range(n):
  integral.append(h*f(a +h/2 + i*h))
 resultado = sum(integral)
 return resultado
def trap(a,b,f,n):
 h = (b-a)/n
 integral = [(f(a)+f(b))/2]
 
 for i in range(1,n):
  integral.append(f(a+h*i))
 resultado = sum(integral)*h
 return resultado
def simp(a,b,f,n):
 h = (b-a)/n
 integral = [(f(a)+f(b))]
 for i in range(1,n):
  if i % 2 == 0:
   integral.append(f(a+i*h)*2)
  else:
   integral.append(f(a+i*h)*4)
   
 resultado = sum(integral)*(h/3)
 return resultado
def quad(a,b,f,n):
 x,w = gaussxwab(n,a,b)
 integral = []
 for i in range(n):
  integral.append(w[i]*f(x[i]))
 resultado = sum(integral)
 return resultado
def tabela(N,ret,trap,simp,quad,f):
 print(f'{N:^5}',f'{ret(a,b,f,N):>6.15f}',f'{trap(a,b,f,N):>6.15f}',f'{simp(a,b,f,N):>6.15f}',f'{quad(a,b,f,N):>6.15f}')
  
print("N      ret.              trap.             simp.             gauss")
N = []
RET = []
TRAP = []
SIMP = []
QUAD = []

xmax = 60
dx = (b-a)/xmax
x = []
y = []
x0 = [0,65]
y0 = [4.4,4.4]
xmin =4

for i in arange(a,b+dx,dx):
 x.append(i)
 y.append(f(i))

for n in (list(arange(2,xmax+2,2))):
 tabela(n,ret,trap,simp,quad,f)
 N.append(n)
 RET.append(ret(a,b,f,n))
 TRAP.append(trap(a,b,f,n))
 SIMP.append(simp(a,b,f,n))
 QUAD.append(quad(a,b,f,n))
 

FontP = FontProperties()
FontP.set_size('x-small')
subplots_adjust(hspace=0.3,wspace=0.2)
subplot(2,1,1)
plot(x,y,color = 'black')
xlabel('$x$')
ylabel('$f(x) = x^4 -2x +1 $')
grid(True)
xlim(a,b)

subplot(2,1,2)
scatter(N,RET,color='red',label='Retangulo')
scatter(N,TRAP,color='blue',label='Trapézio')
scatter(N,SIMP,color='green',label='Simpson')
scatter(N,QUAD,color='orange',label='Gauss')
plot(x0,y0, color='black', label='exato')
legend(prop = FontP)
suptitle("Diferentes métodos de integração",fontsize=14)
xlabel("N intervalos",fontsize=12)
ylabel("Integral ",fontsize=12)
xlim(xmin-5,xmax+5)
ylim(xmin,5)
show()