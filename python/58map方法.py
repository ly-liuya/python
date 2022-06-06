# map
list1 = [23, 45, 6, 7, 8, 93]


# 需求，将list1中的每个数据分别加上3
# map():第一个参数：是一个函数，第二个参数是一个可迭代对象
# 返回值：是一个map类型的对象
def add(x):
    return x + 3


list2 = map(add, list1)
#       map(lambda x, x+3, list1)
print(list(list2))
