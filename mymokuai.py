__all__ = ["test1","test2"] # import * 只有test1，2功能
def test1(a,b):
    print(a + b)

def test2(a,b):
    print(a - b)

def test3(a,b):
    print(a * b)

def test4(a,b):
    print(a / b)

if __name__ == "__main__":  # 测试模块效果
    test1(1,2)
    test2(1,2)
    test3(1,2)
    test4(1,2)
