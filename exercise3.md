# 第三次作业
## 摘要  
解答课后作业1.1题，并尝试在第一题背景下解决1.2题问题，主要定义了使速度与路程增加的函数，并使用while循环结构，以h=0.02为间距输出不同时刻的速度与路程。
## 背景介绍  
1.1题要求使用欧拉法解加速度为定值时的速度，而1.2题则要求使用欧拉法解速度为定值时的路程。欧拉法的核心是以直代曲，而这两道题目中的函数图像均为直线，用欧拉法得到的的结果
 与预期完全一样。为使所解决问题跟体现欧拉法的思想，这里我将1.2题的问题放入1.1中，即1.2中的速度与1.1中一样再来比较计算结果与预期结果的区别。
##正文  
```
def velocity_v(v,h):
    velocity=v+9.8*h
    return velocity # 定义速度函数
def distance_x(x,h):
    distance=x+v*h
    return distance # 定义位移函数
x=0.0
v=0.0
t=0.0
h=0.02
#定义各参量初值
while 0.0<=t<=10.0:
    t=t+h
    v=velocity_v(v,h)
    x=distance_x(x,h)
    print('t=',t,  'v=',v,  'x=',x)
    #输出速度，位移及对应时刻
 ```
 这里是代码链接https://github.com/KKllc/computationalphysics_N2015301020021/blob/master/velocity%2Bdistance.py
## 结论 
 整个过程计算得出的v与预期完全一致，得出的x则在t较小时有较大的相对误差，到t接近10时误差已经较小，若将h取的更小或t取的更大，结果会更接近。
