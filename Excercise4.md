#  第四次作业
## 摘要
2.6题，在不考虑空气阻力的情况下的炮弹出射运动
## 背景
利用欧拉法得出不同时刻的炮弹x坐标与y坐标，并绘图，调整出射角度后，再绘图进行比较。
## 正文
选定了40度到50度之间的一系列角度，45度落点最远与预期一样
[效果图](https://github.com/KKllc/computationalphysics_N2015301020021/blob/master/Figure_1.png)  
对应源代码  
'''  
import math
import matplotlib.pyplot as plt
g=9.8
u=750
theta=40
t=0
x=0
y=0
h=0.005
X1=[0]
Y1=[0]
T1=[0]
while t<=500:
    x=x+u*math.cos(math.radians(theta))*h
    y=y+(u*math.sin(math.radians(theta))-g*t)*h
    t=t+h
    T1.append(t)
    X1.append(x)
    Y1.append(y)
    if y<0:
        break
plt.plot(X1,Y1, label='40')
plt.legend()
plt.xlabel('x/m')
plt.ylabel('y/m')
plt.show()  

'''
## 总结  
语言上的知识仍然匮乏，目前只能写到这种程度，很抱歉。。。

