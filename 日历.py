import calendar
y = int(input("请输入年份:"))
m = int(input("请输入几月份日历:"))
cal = calendar.month(y,m)
print(f"{y}年{m}月的日历:")
print(cal)
