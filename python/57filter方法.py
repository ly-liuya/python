# filter 是一个内置类
ages = [12, 34, 56, 77, 89, 43, 25, 32]

# 将ages列表中，数据值大于30的数字筛选出来
# filter() 有两个参数，第一个参数是一个函数，第二个参数是一个可迭代对象
# 返回值是一个filter类型的对象

def isdy(n):
    return n > 30

list1 = filter(isdy, ages)
# print(list1)
"""
for i in list1:
    print(i)
"""

print(list(list1))  # list() 将其他类型转换为列表类型

