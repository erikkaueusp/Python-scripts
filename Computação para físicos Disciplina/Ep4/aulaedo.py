from numpy import e, sqrt, log


def f(x):
 return sqrt(1-log(x))
 

x = 0.97
y = f(x)
while y != x :
 print(x)
 y = x
 x = f(x)
 