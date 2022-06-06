# 闭包函数
# 如果一个函数里面嵌套了另外一个函数，外部的函数叫做外函数，
# 内部的函数叫做内函数
#   如果在一个外部函数中，定义了一个内部函数，
#   并且外部函数的返回值是内部函数，就构成了一个闭包，
#   则这个内部函数被称为闭包

# 最简单的闭包
def outer():
    def inner():
        print("我是闭包函数")

    return inner  # 这里返回的是函数体，不是函数的调用


fn = outer()  # fn  ===> inner函数


# fn()  # 相当于调用了inner函数

# 闭包的小练习
def outer1(x):
    y = 11

    def inner1():
        print(x + y)

    return inner1()


func1 = outer1(7)

func1()

# 闭包函数主要用于装饰器函数的实现
