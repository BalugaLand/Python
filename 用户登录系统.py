def main():
    shouci =open("flag.txt", "r", encoding="UTF-8").read()
    if shouci=="0" :
        print("首次登录！")
        pass
    elif shouci=="1":
        print("欢迎回来！")
        pass
    else:
        print("初始化错误!")
        pass

def chushihua():
    pass
def user_select():
    pass
def login():
    pass

if __name__ == "__main__":
    main()
