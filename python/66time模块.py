# time模块，主要用来操作时间，time模块不仅仅可以用来显示时间，还可以控制程序
import time
print(time.time())  # 获取从1970年1月1日 0 时 0 分 0 秒距今经历的秒数
print(time.strftime("%Y-%m-%d %H:%M:%S"))  # 按照格式显示日期时间

print("hello")
time.sleep(5)  # 让程序暂停5秒后再执行

print("world")
