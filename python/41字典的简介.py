# 使用列表存储多个数据的时候，在获取或者修改的时候存在一些缺陷，可以使用字典解决

# list1 = ["张三",32,175,"男","清华大学","算法工程师"]

# 字典的语法：{key:value,key1:value2}

dict1 = {"name":"张三","age":"32","height":175,"sex":"男","school":"清华大学","job":"算法工程师"}
print(dict1)

# 访问字典中的元素,
# 第一种方式：通过索引的方式访问字典中的元素
print(dict1['name'])
print(dict1['job'])

# 第二种方式：get()
print(dict1.get('age'))
print(dict1.get('money')) # None 访问不存在的key时，返回的是 None

# 修改字典中的元素
dict1["name"] = "张大锤"
print(dict1)

# 向字典中添加元素
dict1["money"] = 55000
print(dict1)

# 向字典中删除元素
# 第一种方式：pop('要删除元素的key'),删除指定key对应的
dict1.pop("school")
print(dict1)

# 第二种方式：popitem(),随机返回并删除字典中的一对键和值
dict1.popitem()
print(dict1)

# 第三种方式：clear() 清空字典
dict1.clear()
print(dict1)



#