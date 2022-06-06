# 需求：给如下的函数添加功能
# 在函数中，多输出一句话："我很好"
# def test():
#     print("你好吗？")
#

# test()


# 第一种实现的方式：修改了原来的函数
"""def test():
    print("你好吗")
    print("我很好")


test()
"""

# 第二种实现方式:定义一个新函数，在新函数中，先调用原函数，然后在追加功能
"""def demo():
    test()
    print("我很好")


demo()"""


# 还可以在程序运行的过程中，动态的添加功能，使用装饰器实现
# a.此处的outer函数就是一个装饰器函数
# b.fn 表示形参，实际调用装饰器函数的时候，传入的实际参数是原函数的名字
def outer(fn):
    def inner():
        fn()  # c.调用原函数
        print("我很好")  # d.给原函数添加功能,添加的功能可以写在原函数的上面也可以写在元函数的下面

    return inner


# 最普通的调用
# test = outer(test)
# test()

# 装饰器的简写方式 @+装饰器名称
# 原函数：
@outer  # 等价于 test = outer(test)
def test():
    print("你好吗？")


test()

"""
注意：
1、原函数必须在装饰器函数的下面
2、outer函数就是装饰器函数 @outer
"""