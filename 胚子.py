import random
bjl_1   =[2.7,3.1,3.5,3.9]
bjsh_1  =[5.4,6.2,7.0,7.8]
ysjt_1  =[16,19,21,23]
GJL_1   =[4.1,4.7,5.3,5.8]
FYL_1   =[5.1,5.8,6.6,7.3]
SMZ_1   =[4.1,4.7,5.3,5.8]
gjl_1   =[14,16,18,19]
fyl_1   =[16,19,21,23]
smz_1   =[209,239,269,299]
yscnxl_1=[4.5,5.2,5.8,6.5]
a=[0,0,0,0,0,0,0,0,0,0,0]
for i in range(11):
    a[i]= random.randint(0,3)
bjl_2 = bjl_1[a[1]]
bjsh_2 = bjsh_1[a[2]]
ysjt_2 = ysjt_1[a[3]]
GJL_2 = GJL_1[a[4]]
FYL_2 = FYL_1[a[5]]
SMZ_2 = SMZ_1[a[6]]
gjl_2 = gjl_1[a[7]]
fyl_2 = fyl_1[a[8]]
smz_2 = smz_1[a[9]]
yscnxl_2 =yscnxl_1[a[10]]

bl = "暴击率+"
bs = "暴击伤害+"
jt = "元素精通+"
GJL = "攻击力(%)+"
FYL = "防御力(%)+"
SMZ = "生命值(%)+"
gjl = "攻击力+"
fyl = "防御力+"
smz = "生命值+"
yscnxl = "元素充能效率+"

peizi=[]
citiaoshu = random.randint(3,4)
citiao_1 = [f"{bl}{bjl_2}%" ,f"{bs}{bjsh_2}%",f"{jt}{ysjt_2}",f"{GJL}{GJL_2}%", f"{FYL}{FYL_2}%" ,
            f"{SMZ}{SMZ_2}%" ,f"{gjl}{gjl_2}" ,f"{fyl}{fyl_2}",f"{smz}{smz_2}",f"{yscnxl}{yscnxl_2}%"]
peizi = random.sample(citiao_1,k=citiaoshu)
for i in range(citiaoshu):
    if peizi[i-1] == f"{GJL}{GJL_2}%":
        peizi[i-1] = f"攻击力+{GJL_2}%"
    elif peizi[i-1] == f"{FYL}{FYL_2}%":
        peizi[i-1] = f"防御力+{FYL_2}%"
    elif peizi[i-1] == f"{SMZ}{SMZ_2}%":
        peizi[i-1] = f"生命值+{SMZ_2}%"
    else:
        pass
Peizi = "\n".join(peizi)
print(Peizi,"\n")
print("强化一次...\n")
