# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 14:47:17 2017

@author: hp
"""

import math
import matplotlib.pyplot as plt
theta=30
theta_radians=math.radians(theta)
alerfa=0
omiga=2.0
v=30
g=9.8
vx=v*math.cos(theta_radians)
vy=v*math.sin(theta_radians)
vz=0
x=0
y=1.5
z=0
t=0
X=[0]
Y=[0]
Z=[0]
h=0.005
while t<500:
    x=x+vx*h
    y=y+vy*h
    z=z+vz*h
    t=t+h
    X.append(x)
    Y.append(y)
    Z.append(z)
    v=math.pow((vx*vx+vy*vy),0.5)
    vz=vz+(0.5*(math.sin(4*alerfa)-0.25*math.sin(8*alerfa)+0.08*math.sin(12*alerfa)-0.025*math.sin(16*alerfa)*g))*h
    vx=vx-(0.0039+0.0058/(1+math.exp((v-35)/5)))*h
    vy=vy-g*h
    alerfa=alerfa+omiga*h
    if y<0:
        break
plt.plot(X,Z,label='omiga=2.0rad/s')
#plt.plot(X,Y,label='y')
plt.xlabel('x/m')
plt.ylabel('z/m')
plt.title('Knuckleballs` Horizontal Deflection of z(m)-x(m)')
plt.legend()
plt.show()