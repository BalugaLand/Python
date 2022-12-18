import numpy as np
import matplotlib.pyplot as p
x=[]
y=[]
for i in range(1250):
    x.append(i)
    y.append(i*np.sin(i))
p.plot(x,y,linewidth=2)     # 设置线宽度
p.xlabel("x")
p.ylabel("sin")
p.rcParams["font.sans-serif"]=["SimHei"]    # 设置字体用于正常显示中文标签
p.title("多点折线图")
p.savefig("sin_i.png")
p.show()
