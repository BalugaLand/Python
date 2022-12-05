import os
f_name = "普通用户文件夹"
if not os.path.exists(f_name):
    os.mkdir(f_name)

def main():
    f =open("flag.txt", "r", encoding="UTF-8")
    shouci = f.read()
    if shouci=="0" :
        print("首次登录！")
        c_f()
        init()  # 管理员初始化函数
        login() # 选择用户类型
        user_select()   # 用户选择


        pass
    elif shouci=="1":
        print("欢迎回来！")
        login()
        user_select()

        pass
    else:
        print("初始化错误!")
        pass
    f.close()

def c_f():
    f = open("flag.txt","w")
    f.write("1")
    f.close()

def init():
    file_1=open("u_root.txt","w")
    root={"zhanghao":"root","password":"1234"}
    file_1.write(str(root))
    file_1.close()

def login():
    print("""----用户选择----
1-管理员登录
2-普通用户登录
---------------""")

def user_select():
    while True:
        s = input("请选择用户类型:")
        if s == "1":
            print("管理员登录...")
            root_login()    # 管理员登录
            break
        elif s == "2":
            print("普通用户登录...")
            select = input("是否需要注册？(y/n):")
            if select == "Y" or select == "y":
                print("****用户注册****")
                user_register()
                break
            elif select == "N" or select == "n":
                print("****用户登录****")
                user_login()
                break
            else:
                print("选择有误，重新选择!")


        else:
            print("选择有误，重新选择!")
            # user_select() # 代替while True

def root_login():
    print("****管理员登录****")
    r_zhanghao = input("请输入用户名:")
    r_password = input("请输入密码:")
    file_root = open("u_root.txt","r")
    root = eval(file_root.read())
    file_root.close()
    if r_zhanghao == root["zhanghao"] and r_password == root["password"]:
        print("管理员登录成功！")
    else:
        print("密码错误，重新登录!")
        root_login()

def user_register():
    user_id = input("请输入用户名:")
    user_pwd = input("请输入密码:")
    user_name = input("请输入昵称:")
    user = {"u_id":user_id,"u_pwd":user_pwd,"u_name":user_name}
    user_path = f_name+"/"+user_id
    u = open(user_path,"w")
    u.write(str(user))
    u.close()
def user_login():
    print("****普通用户登录****")
    user_id = input("请输入你的用户名:")
    user_pwd = input("请输入你的密码:")
    u_list = os.listdir(f_name)
    if user_id in u_list:
        print("登录中...")
        file_path = f_name+"/"+user_id
        file_path = open(file_path,"r")
        file_path = file_path.read()
        file_path = eval(file_path)
        if user_pwd == file_path["u_pwd"]:
            print("登录成功!")
        else:
            print("密码错误，登录失败!")
    else:
        print("查无此人!请先注册!")




if __name__ == "__main__":
    main()
