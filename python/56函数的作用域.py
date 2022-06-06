# 作用域：变量能够生效的范围
if 5 > 4:
    a = 11
print(a)

for i in range(1, 11):
    b = 77
print(b)


def fn():
    c = 87


# print(c)
# 总结：
# 1、if等分支语句和for in 等循环语句不存在作用域问题，
# 他们里面定义的变量可以在外部直接访问
# 2、函数内部的变量，在函数的外部不能直接访问
# 3、函数内部可以直接访问函数外部的变量
# 4、
num = 99


def demo():
    print(num)


demo()  # 99

num1 = 67


def fn1():
    # 若想在函数的内部直接修改外部的变量，
    # 需要使用global关键字，将函数内部变量变更为全局变量
   global  num1
   num1 = 88
   print(num1)


fn1()  # 88
# print(num1)  # 67  是在函数内部，无global时
print(num1)