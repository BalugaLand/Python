import datetime
time1 = datetime.datetime.now()         # 获取现在时间
time2 = datetime.datetime.today()       # 获取今天的时间
time3 = datetime.datetime.utcnow()      # 获取世界标准时间
print(time1)
print(time2)
print(time3)
time4 = datetime.date(2022,11,1)        # 创建日期
time5 = datetime.time(20,0,0)           # 创建时间
time6 = datetime.datetime(2022,11,11,11,11,11)  # 创建时间与日期
print(time4)
print(time5)
print(time6)
