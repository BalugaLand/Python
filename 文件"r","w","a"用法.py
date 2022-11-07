f = open(file = "D:/测试2.txt",mode="w",encoding="UTF-8") # 从头写
f.write("你好你好Baluga\n")
f = open(file = "D:/测试2.txt",mode="a",encoding="UTF-8") # 添加
f.write("MHHarry MHydd")
f = open(file = "D:/测试2.txt",mode="r",encoding="UTF-8") # 读取
print(f.read())
f.close()
