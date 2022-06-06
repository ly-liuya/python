# datetime 主要用来显示日期时间,其中date类用来显示日期,time类用来显示时间
import datetime
print(datetime.date(2019,2,11))  # 创建一个日期
print(datetime.time(11,21,25))   # 创建一个时间
print(datetime.datetime.now())   # 获取当前的日期时间
print(datetime.datetime.now() + datetime.timedelta(5))  # 获取5天后的时间
