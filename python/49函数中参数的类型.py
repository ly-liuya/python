# 参数的类型：
# a.必须参数
# 在调用函数的时候，必须以正确的顺序传参，参数数量保持一致
def student(name,age):
    print("我的姓名是：%s,年龄是：%d"%(name,age))

# student("王麻子",32)
# student(32,"王麻子") 类型不对
#TypeError: %d format: a number is required, not str

# b.关键字参数
# 使用关键字参数允许函数调用的时候，实参的顺序和形参的书序不一致，可以使用关键字
# 进行自动匹配
# student(age=32,name="王麻子")


# c.默认参数
# 1、在定义函数时，若某个参数没有传递，但是定义了默认参数，会直接使用默认参数
# 若传递了参数，则会把默认参数替换
# 2、若函数设置了默认参数，并且该函数有多个参数，一般把默认参数列表的后面
def get_sum(num1,num2,num3=21):
    print(num1+num2+num3)

get_sum(12,34,56)  #102
get_sum(12,34)    #67
get_sum(1,2,3)   #6