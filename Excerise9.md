# 第九次作业
## 摘要
利用弛豫法模拟电势分布，经多次迭代后达到稳定。
## 背景
将需要模拟的区域划分为有限数目的区块，根据要求对相应区块设置对应边界条件，然后进行迭代，在保证边界区域初始值基础上，其他各点的值在每一次迭代中等于上一次它相邻四周边角上四点的平均值
## 内容
由于上周忘记了作业，这里只取了5.4数据下的背景模拟，在这里感谢刘庆康同学对于这个模拟原理，以及代码实现方式的讲解。下面是效果，迭代到30次以后图形完全稳定了下来。
![](https://github.com/KKllc/computationalphysics_N2015301020021/blob/master/chiyu.png)  
左图为迭代20次后的结果，右图是迭代75次后完全稳定的结果.  
下面是完整代码：
```
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

the_origin_v=[[0 for col in range(76)] for row in range(76)]
for i in range(19,56):
    for j in range(19,56):
        the_origin_v[i][j]=1

for i in range(0,75):
    the_origin_v[0][i]=0
    the_origin_v[75][i]=0

for i in range(0,75):
    the_origin_v[i][75]=0
    the_origin_v[i][0]=0

V=[the_origin_v]

for i in range(0,100):
    Vn=V[i]
    K=[[0 for col in range(75)] for row in range(75)]
    for i in range(1,74):
        for j in range(1,74):
            if (Vn[i][j]!=1 and Vn[i][j]!=-1):
                K[i][j]=round((Vn[i-1][j]+Vn[i+1][j]+Vn[i][j-1]+Vn[i][j+1])/4,2)
    for i in range(0,75):
        for j in range(0,75):
            K[i][j]=K[i][j]+V[0][i][j]
    V.append(K)



x=[]

for i in range(0,75):

    x.append([i for j in range(0,75)])

X=sum(x,[])



y=[]

for i in range(0,75):

    y.append([i for i in range(0,75)])

    

Y=sum(y,[])

Z1=sum(V[20],[])

Z5=sum(V[75],[])




fig = plt.figure(figsize=(12,6))

ax1 = fig.add_subplot(121,projection='3d')

ax2 = fig.add_subplot(122,projection='3d')



ax1.scatter(X,Y,Z1,s=2)



ax2.scatter(X,Y,Z5,s=2)




plt.show()
```
其他图形改变边界条件即可。
