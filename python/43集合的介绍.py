# 1、python中的集合和数学中的集合比较类似
# 特点：无序，无重复元素的集合

# 1、创建集合
set1 = {12,34,5,67,True}
print(set1)
print(type(set1))  # <class 'set'>

# 2、集合不能通过下标访问或修改
# print(set1[1])
# set1[1] =98

# 3、获取集合的长度 len()
print(len(set1))  # 5

# 4、向集合中添加元素 add(),只能一次性添加一个元素
# set1.add(98)
# set1.add(57)
# print(set1)

# 5、update() 可以一次向集合中添加多个元素 ,追加的数据以列表的形式添加
set1.update([76,2,3])
print(set1)

# 6、删除集合中的元素
# 第一种：pop(), 随机删除一个元素
set2 = {23,45,67,8,90,87}
# set2.pop()
# print(set2)

# 第二种：remove(),删除指定的元素，要传入删除的元素的值,若删除不存在的元素，直接报错
# set2.remove(45)
# set2.remove(99)
# print(set2)

# 第三种：discard(),删除指定的元素，要传入删除元素的值，若删除不粗安在的元素，不会报错
set2.discard(8)
set2.discard(99)
print(set2)

# 第四种：clear() 清空集合
# set2.clear()
# print(set2)

# 7、遍历集合
for i  in set2:
    print(i)

