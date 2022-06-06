# 函数按照有没有名字分为：有名字的函数和匿名函数

#有名字的函数
def test():
    print("有名字的函数")
test()

# 匿名函数：是一个表达式，比普通函数简单,使用lambda定义的表达式
# lambda表达式中，包含了参数，实现体，返回值
def fn(num):
    return num ** 2

print(fn(3))
# lambda
num1 = lambda num:num ** 2
print(num1(4))
