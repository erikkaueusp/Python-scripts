#Erik Kaue  Número usp:8516455
#nBalística 
from numpy import pi,sin,cos #biblioteca para valor de pi e funções seno e cosseno.

theta = float(input("Digite um valor em graus º: "))
radiano = (theta*pi/180) # fórmula para converter um valor em grau para radiano.
v = float(input("Digite uma velocidade: (m/s): "))
def balística(v,radiano): #função definidida para calcular o valor de Hmax e Rmax obtidos através das equações de movimento.
 g = 9.8 #constante da gravidade
 H = ((v*sin(radiano))**2)/g
 R = (v**2)*sin(2*radiano)/g
 
 print("Os respectivos valores de H max e R em metros são: %f metros e %f metros" % (H,R))

balística(v,radiano)