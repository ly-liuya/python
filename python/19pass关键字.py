# pass关键字在python中没有任何意义，只是单纯的实现占位，保证语句的完整性
age = int(input("请输入你的年龄："))
if age > 18:
   # print("欢迎光临")
    pass #使用pass进行占位，没有意义，仅仅为了正常运行系统
print("hello world")