# 函数按照有没有返回值分为：有返回值的函数和无返回值的函数

#无返回值的函数
def fn():
    print("hello world")
fn()

#有返回值的函数：
"""
1、函数返回值需要使用return关键字进行返回
函数在哪儿调用，就把结果进行返回到了哪里.若想使用返回值得结果，
可以定义变量接收，也可以直接输出
2、return 后面的代码不会执行,函数发哦return就结束了
3、函数中若没有return关键字或者没有数据返回，则默认返回的是None
4、return关键字， 一次性返回多个数据,
   多个数据之间用,隔开,结果以元组形式返回
5、
   
"""
def test():
    return "我是有返回值得函数"
    print("123")

cc =test()
# print(cc)
# print(test())

def demo():
    return

print(demo())


def demo1():
    print("你好啊")
print(demo1()) # None

#  return关键字， 一次性返回多个数据,
#  多个数据之间用,隔开,结果以元组形式返回
def fn1():
    return 12,32,45,
print(fn1())
