#  break 和 continue关键字，主要用于python中的循环程序中
# break 是用来结束整个循环,一般用于死循环中，结束循环执行
# continue 是跳出当前循环，开启下一轮循环

#1、当num == 3 的时候，后续的num的值不输出
"""
num = 0
while num < 5:
    if num == 3:
        num += 1
        break
    print(num)
    num += 1
最终输出结果： 0 1 2
"""

#2、当num == 3 的时候，不输出整个值，继续后续的输出
"""
num = 0
while num < 5:
    if num == 3:
        num += 1
        continue
    print(num)
    num += 1
"""

#死循环，无法终止循环的终止条件
#1、输入用户名和密码？只有当用户名和密码正确以后停止输入，否则一直输入
#正确用户名和密码：张三 123456
while True:
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if username == "张三" and password =="123456":
        print("恭喜您，账号密码正确，欢迎您")
        break
    else:
        print("用户名密码错误，请重新输入")
