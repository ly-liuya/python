# 排序
list1 =[12,34,56,6,3,72]
# 1、sort() 对原列表中的元素进行排序，默认是升序，不会生成一个新的列表
# 实现降序排列，传入参数reverse=True
# list1.sort() # 升序
# print(list1)
# list1.sort(reverse=True)  # 降序
# print(list1)

# 2、sorted() 对列表元素进行排序(默认升序),排序的结果是一个新的列表
list2 = sorted(list1)  # 升序
# print(list2)
list3 = sorted(list1,reverse=True)
# print(list3)

list4 = ["abc","hello","e","love","mm"]
# 按照列表元素的长度进行排序
list5 = sorted(list4,key=len)
# print(list5)

# 3、翻转列表
list6 = [12,34,56,234,45,23,21]
# list.reverse() 	反向列表中元素
list6.reverse()
print(list6)

# 4、获取列表长度 len()
list7 = [32.4,54,5,7,"hello","True"]
print(len(list7)) # 6

# 5、获取列表中的最大值 max(list)
list8 = [32,43,5454,65,789,43]
print(max(list8))  # 5454

# 6、获取列表中的最小值 min(list)
print(min(list8))  # 32

# 7、获取列表指定元素的索引 index()
print(list8.index(5454))  #  2