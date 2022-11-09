t1 = open("D:/bill.txt","r",encoding="UTF-8")
t2 = open("D:/bill2.txt","w",encoding="UTF-8")
for line in t1:
    if line.strip().split(",")[2] == "测试":
        continue
    else:
        t2.write(line)
t1.close()
t2.close()
