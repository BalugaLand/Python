import matplotlib.pyplot as p
import numpy as np
x=np.linspace(0,10,100)     # 生成0~10之间100个等差数列
y=np.sin(x) # 设置y的值为y=sin(x)
p.scatter(x,y,s=20,c="yellow",alpha=0.6) # 绘制散点图
p.show()
