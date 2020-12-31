import vpython as vp
import numpy as np
L =1
r = 0.3
for k in range(-L,L+1):
 if abs(k) == L or k == 0 :
  for j in range(-L,L+1):
   if abs(j) == L or j ==0 :
    for i in range(-L,L+1):
     if abs(i) == L or i==0 :
      if (i,j,k) != (0,0,0) and abs(i) + abs(j) + abs(k) != 2*L :
       vp.sphere(radius = 0.3,pos=vp.vector(i,j,k),color = vp.vector(1,0,0))