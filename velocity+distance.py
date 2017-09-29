# -*- coding: utf-8 -*-
def velocity_v(v,h):
    velocity=v+9.8*h
    return velocity
def distance_x(x,h):
    distance=x+v*h
    return distance
x=0.0
v=0.0
t=0.0
h=0.02
while 0.0<=t<=10.0:
    t=t+h
    v=velocity_v(v,h)
    x=distance_x(x,h)
    print('t=',t,  'v=',v,  'x=',x)
