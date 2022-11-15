def f1():
    print("开始f1")
    1 / 0
    print("结束f1")
def f2():
    print("开始f2")
    f1()
    print("结束f2")
def main():
    try:
        f2()
    except Exception as e:
        print(f"异常是{e}")
main()
