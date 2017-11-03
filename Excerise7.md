# 第七次作业
## 摘要
利用课本给出的logistic模型，对混沌现象的产生原因进行模拟与探讨，对应课后3.23题。
## 背景介绍
logistic模型给出了一个简单的迭代关系式Xn+1=μx（1-x），在图上同时绘制Xn——Xn与Xn——Xn+1图像或Xn——Xn+2图像，观察交点，了解其意义。
## 正文
这里主要针对Xn与Xn+2来绘制一些图，看一下在不同μ下的固定点  
首先是μ=2.00时  
![](https://github.com/KKllc/computationalphysics_N2015301020021/blob/master/%CE%BC%3D2.00.png)  
此时只有一个固定点...和Xn+1的关系差不多...  
μ=2.35时  
![](https://github.com/KKllc/computationalphysics_N2015301020021/blob/master/%CE%BC%3D2.35.png)  
也一样。后面依次为μ等于2.65与3.00时的图像，3.00时开始出现了进一步弯曲。  
![](https://github.com/KKllc/computationalphysics_N2015301020021/blob/master/%CE%BC%3D2.65.png)  
![](https://github.com/KKllc/computationalphysics_N2015301020021/blob/master/%CE%BC%3D3.00.png)  
而且，μ=3.0的一部分片段两条曲线完全相切了...这应该和的是课本上Xn在两个值之间震荡的情况类似吧，还是比较稳定的震荡。  
μ=3.35时已经出现了三个交点，  
![](https://github.com/KKllc/computationalphysics_N2015301020021/blob/master/%CE%BC%3D3.35.png)  
这里我们就可以看到在中间的交点处出现了课本上的不稳定的固定点区域，在该点附近的点会反复出现细微重复的变化，造成了混沌现象中初始值引起较大后来值改变。  
μ=3.85时更为明显：  
![](https://github.com/KKllc/computationalphysics_N2015301020021/blob/master/%CE%BC%3D3.85.png)
代码很简单，如下：
```
import matplotlib.pyplot as plt
h=0.001
LIM=1000
μ=3.85
X=[0 for x in range(0,LIM)]
Y=[0 for x in range(0,LIM)]
Z=[0 for x in range(0,LIM)]
X[0]=0
Y[0]=0
Z[0]=0
for i in range(0,LIM-1):
    X[i+1]=X[i]+h
    Y[i+1]=μ*X[i+1]*(1-X[i+1])
    Z[i+1]=μ*Y[i+1]*(1-Y[i+1])
plt.plot(X,X)
plt.plot(X,Z)
plt.xlabel('Xn')
plt.ylabel('Xn+2')
plt.title('Xn+2 vs Xn,μ=3.85')
plt.show()

```
## 结论 
这个模型很好的用迭代给混沌产生原因做了解释。
