# 元组和列表有些类似，本质上也是一种有序的集合
# 元组和列表的不同之处
# 1、元组 () 列表 []
# 2、元组中的元素不能修改

# 1、创建元组,元组中的元素可以是各种数据类型
tup = (12,34,6,7,True,"hello")
print(tup)
print(type(tup)) # <class 'tuple'>

# 注意：若创建元组的时候，只有一个元素，需要在元素的后面加上一个逗号
tup1 = (32,)
print(tup1)

# 2、访问元组元素，通过下标
# print(tup[1]) # 访问第一个元素
# print(tup[-1]) # 访问最后一个元素

# 3、不能修改元组中的元素,会报错
# tup[1] = 876
# print(tup)

# 4、合并元组 通过 +
tup2 = (223,45,6,7)
tup3 = (55,"world",True)
print(tup2 + tup3)

# 5、判断元素是否在元组中，使用成员运算符，in 或者 not in
# print(45 in tup2)   # True
# print(45 not in tup3)   # True

# 6、元组的切片 [开始下标：结束下标]
# print(tup2[0:2])
# print(tup2[-1:])
# print(tup2[:3])

# 7、获取元组的长度 len()
print(len(tup2))  # 4

# 8、获取元组中的最大值 max() 最小值 min()
tup4 =(23,45,6,7,97)
# print(max(tup4))
# print(min(tup4))

# 9、其他数据类型转换为元组 tuple()
list1 =[234,54,6,7]
# print(type(list1))  # <class 'list'>
# tuple(list1)
# print(type(tuple(list1)))  #  <class 'tuple'>


# 10、遍历元组
"""
# 第一种： for in
for i  in tup4:
    print(i)
"""
# 第二种：enumrate
for k,v in enumerate(tup4):
    print(k,v)




