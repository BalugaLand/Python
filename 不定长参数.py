def t(*args):
    print(f"{args},类型是{type(args)}")
t(1,12,34,"哈")

def u(**kwargs):
    print(f"{kwargs},类型是{type(kwargs)}")
u(name="Baluga",age = 18)
