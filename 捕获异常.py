# try:                              
#     f = open("D:/bucunzai1.txt","r",encoding="UTF-8")
#     print("有")
# except:
#     print("文件无")
#     f = open("D:/bucunzai1.txt","w",encoding="UTF-8")
#     f.write("哈哈")


try:                                        # 捕获指定异常
    print(a)
except(NameError) as e:   # 没有变量a输出except后的内容
    print("不存在a")

    
 
try:                                        # 捕获多个异常
    # print(a)
    b = 1/0
except(NameError,ZeroDivisionError) as e:   # 没有变量a 或者 除以0无意义 的异常
    print("异常")
