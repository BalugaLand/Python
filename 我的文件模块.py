def file_info(file_name):
    f = None
    try:
        f = open(file_name,"r",encoding="UTF-8")
        print("文件的内容如下:\n" + f.read())
    except Exception as e:
        print(f"文件出现异常，异常是{e}")
    finally:
        if f:
            f.close()

if __name__ == "__main__":
    file_info("D:/bill.txt")

def file_append(file_name,data):
    t = open(file_name,"a",encoding="UTF-8")
    t.write(data+"\n")
    t.close()

if __name__ == "__main__":
    file_append("D:/bill.txt","jzl")
