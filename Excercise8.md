# 第八次作业
## 摘要
尝试按照课后习题绘制太阳，木星和地球在相互引力作用影响下的运行轨迹的问题。
## 正文
由于个人能力限制，在这次的作业中，Spyder按照设定程序绘制图像时，总会出现“ZeroDivision Error”，即分母位置出现0，按照设定的程序应该是哪两个星球“相撞”了，我在最开始使用的是太阳地球月亮的模型，首先出现了这个错误
如下图所示：
![](https://github.com/KKllc/computationalphysics_N2015301020021/blob/master/error.png)  
我在最开始的想法是。月球距离地球的初始距离是0.000256个天文单位，会不会在后面容易装上而导致崩溃，因此又改用了距离太阳初始5.2个天文单位的木星，然而依然出现了上述错误，还是没能找出错误源在哪里，这里只能放上我的源代码了：  
```
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 17:19:42 2017

@author: hp
"""

import matplotlib as plt
import math

LIM = 8400
Xe  = [0 for i in range(0,LIM)]
Ye  = [0 for i in range(0,LIM)]
Re  = [0 for i in range(0,LIM)]
VXe = [0 for i in range(0,LIM)]
VYe = [0 for i in range(0,LIM)]
Xj  = [0 for i in range(0,LIM)]
Yj  = [0 for i in range(0,LIM)]
VXj = [0 for i in range(0,LIM)]
VYj = [0 for i in range(0,LIM)]
Rj  = [0 for i in range(0,LIM)]
Rej = [0 for i in range(0,LIM)]
t=0.01

Xe[0]  = 1
Ye[0]  = 0
Xj[0]  = 5.20
Yj[0]  = 0
Re[0]  = 1
Rj[0]  = 5.20
Rej[0] = 4.20
VXe[0] = 0
VXj[0] = 0
VYe[0] = 2*math.pi
VYj[0] = 0.876*math.pi

for i in range(0,LIM-1):
    Re[i+1] = math.sqrt(Xe[i+1]**2+Ye[i+1]**2)
    Rj[i+1] = math.sqrt(Xj[i+1]**2+Yj[i+1]**2)
    Rej[i+1] =math.sqrt((Xe[i+1]-Xj[i+1])**2+(Ye[i+1]-Yj[i+1])**2)
    VXe[i+1] = VXe[i]-(4*math.pi*math.pi*Xe[i]*t)/(Re[i]**3)-(4*math.pi*math.pi*0.0009552*(Xe[i]-Xj[i])*t)/(Rej[i]**3)
    VYe[i+1] = VYe[i]-(4*math.pi*math.pi*Ye[i]*t)/(Re[i]**3)-(4*math.pi*math.pi*0.0009552*(Ye[i]-Yj[i])*t)/(Rej[i]**3)
    VXj[i+1] = VXj[i]-(4*math.pi*math.pi*Xj[i]*t)/(Rj[i]**3)-(4*math.pi*math.pi*3.005*0.001*(Xj[i]-Xe[i])*t)/(Rej[i]**3)
    VYj[i+1] = VYj[i]-(4*math.pi*math.pi*Yj[i]*t)/(Rj[i]**3)-(4*math.pi*math.pi*3.005*0.001*(Yj[i]-Ye[i])*t)/(Rej[i]**3)
    Xe[i+1] = Xe[i]+VXe[i+1]*t
    Ye[i+1] = Ye[i]+VYe[i+1]*t
    Xj[i+1] = Xj[i]+VXj[i+1]*t
    Yj[i+1] = Yj[i]+VYj[i+1]*t
plt.plot(Xe,Ye)
plt.plot(Xj,Yj)
plt.show()
```
很抱歉，只能做到这一步了。
