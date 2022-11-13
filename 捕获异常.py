# try:                              
#     f = open("D:/bucunzai1.txt","r",encoding="UTF-8")
#     print("有")
# except:
#     print("文件无")
#     f = open("D:/bucunzai1.txt","w",encoding="UTF-8")
#     f.write("哈哈")


try:                                        # 捕获指定异常
    print(a)
except(NameError,ZeroDivisionError) as e:   # 没有变量a输出except后的内容
    print("不存在a")
