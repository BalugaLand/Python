num = 0                                   # 1~100之间取偶数
for i in range(1,100):
    if i % 2 == 0:
        num += 1
print(f"1~100之间（不含100）有{num}个偶数")
