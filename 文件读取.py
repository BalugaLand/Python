with open(file="D:/测试.txt",mode="r",encoding="UTF-8") as f:   # 自动关闭文件,防止忘记f.close()
    # print(f.readline())     # 读一行
    # print(f.read(10))       # 读十个字符
    # print(f.readlines())    # 全读完
    for l in f:
        print(l)
