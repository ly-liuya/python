# 1、一个装饰器函数修饰多个函数
"""# 定义一个装饰器函数，对下面的数学运算函数添加解释说明
def outer(fn):
    def inner(*args):
        print("数学运算的结果是：", end=" ")
        fn(*args)

    return inner


@outer
def add(a, b):
    print(a + b)


@outer
def jian(c, d,e):
    print(c - d - e)


add(12,34)
jian(87,56,1)
"""


# 2、一个函数有多个装饰器函数
def outer1(fn):
    def inner1():
        fn()
        print("唱歌给我听")

    return inner1


def outer2(fn):
    def inner2():
        fn()
        print("哪儿都有你的。。。。。。")

    return inner2


@outer2
@outer1
def say():
    print("唱歌给谁听.....")


say()

# 注意：一个函数被多个装饰器修饰，装饰器是从离原函数最近的开始，原函数只执行一次
