# 可以使用变量来保存我们的数据，一个变量一次只能保存一个数据
"""
name = "张三"
name1 = "李四"
name2 = "王五"

"""
# 可以使用列表一次性保存多个数据 []
# 定义列表
"""
1、列表中的元素可以是不同的数据类型
2、使用[]来声明列表
3、通过下标来访问列表中的元素
"""
list1 =["张三","李四","王五",123,True,False]
print(list1)
# 通过下标获取元素，下标从0开始
print(list1[2])

# 修改列表元素，通过下标修改
list1[2] = "lili"
print(list1)

# 遍历列表
# 第一种方式 for in
"""
for i in list1:
    print(i)
"""
# 第二种方式
for index,value in enumerate(list1):
    print(index,value)
