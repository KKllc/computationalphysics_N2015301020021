# 第六次作业
## 摘要
利用课本上给出的由欧拉——克拉默方法导出的递推公式，探究在阻尼和驱动力作用下，摆的运动出现混沌的现象。
## 背景介绍
这里主要探讨课后题目3.10，在不同F下的摆位置随时间变化的图像，以及摆位置θ与对应角速度所出现的混沌图像。
## 正文
计算中，我取初值绳长l=9m，q=0.5，驱动力圆频率ΩD=2/3,初始位置θ=0.2，以下为一系列驱动力FD所对应的θ-t图像，  
首先是FD=0.1
![](https://github.com/KKllc/computationalphysics_N2015301020021/blob/master/fd%3D0.1.png)  
没有出现什么明显的混沌现象。  
再来看FD=0.5
![](https://github.com/KKllc/computationalphysics_N2015301020021/blob/master/fd%3D0.5.png)  
现象依然不明显。
FD=1.0  
![](https://github.com/KKllc/computationalphysics_N2015301020021/blob/master/fd%3D1.0.png)  
FD=1.5  
![](https://github.com/KKllc/computationalphysics_N2015301020021/blob/master/fd%3D1.5.png)
从这里开始，后期出现了明显的混沌现象。  
我们再来看FD=2.0时的情景  
![](https://github.com/KKllc/computationalphysics_N2015301020021/blob/master/fd%3D2.0.png)  
这里混沌现象在全局已经非常突出，进一步绘制角速度关于角度曲线  
![](https://github.com/KKllc/computationalphysics_N2015301020021/blob/master/fd%3D2.0_theta.png)  
此时的摆位置处于以较难预测的状态.  
值得注意的是，继续增大FD后，后续的图形会变得极为密集，但有些时候仍可以展现出一定规律性，比如FD=2.5与4.0时图线  后期仍显示出了一定规律，  
FD=2.5
![](https://github.com/KKllc/computationalphysics_N2015301020021/blob/master/fd%3D2.5.png)  
FD=4.0  
![](https://github.com/KKllc/computationalphysics_N2015301020021/blob/master/fd%3D4.0.png)  
在这里混沌与规律性现象交替出现了。

源代码
```
import math
import matplotlib.pyplot as plt
g=9.8
l=9
q=0.5
fd=2.0
omiga_d=2/3
omiga=0
h=0.05
t=0
LIM=1200
X=[0 for x in range(0,LIM)]
Y=[0 for x in range(0,LIM)]
Z=[0 for x in range(0,LIM)]
X[0]=0
Y[0]=0
Z[0]=0.2
for i in range (0,LIM-1):
    X[i+1]=X[i]+h
    Y[i+1]=Y[i]-((g/l)*math.sin(Z[i])+q*Y[i]-fd*math.sin(omiga_d*X[i]))*h
    Z[i+1]=Z[i]+Y[i+1]*h
    if Z[i+1]>math.pi:
        Z[i+1]=Z[i+1]-2*math.pi
    elif Z[i+1]<-math.pi:
        Z[i+1]=Z[i+1]+2*math.pi
plt.plot( Z,Y)
plt.xlabel('theta')
plt.ylabel('omiga')
plt.show()
```  

补充：后来又进一步绘制出一系列以0.05为步长的δθ随时间变换的曲线，从另一个侧面反映了混沌现象的产生。如下为FD=1.5时的δθ随时间变化的图像
![](https://github.com/KKllc/computationalphysics_N2015301020021/blob/master/%CE%B4%CE%B8.png)
## 结论
这次编程过程中，由于一开始将迭代公式中耗散项与驱动力向的正负号搞反，导致图像非常不正常，请教其他同学后并没有找到问题，这里感谢刘庆康同学，改变了原有的append生成数组的方法，变为了更为直观的语言。由于之前的错误浪费的很多时间δθ部分是后来才补上的。从结果来看，在这一组绳长l，驱动力角频率的初值下，

