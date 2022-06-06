#
dict1 = {"name":"中国医生","author":"刘伟强","person":"张涵予","address":"China"}

# 1、获取字典的长度 len()
print(len(dict1))

# 2、获取字典中所有的key  dict1.keys()
print(dict1.keys())

# 3、获取字典中所有的值
print(dict1.values())

# 4、获取字典中所有的key和value
print(dict1.items())

# 5、遍历字典
# 第一种方式：for in
for i in dict1: # 遍历出的是字典中的所有的key
    print(i)

# 第二种方式：遍历字典中所有的key
for k,v in enumerate(dict1):
    print(k,v)

# 第三种方式：遍历字典中所有key和value
for k,v in dict1.items():
    print(k,v)

# 第四种方式：遍历字典中所有的value
for v in dict1.values():
    print(v)

# 6、合并字典 update
dict2 = {"name":"成龙","sex":"男","age":61}
dict3 = {"address":"中国香港"}
dict2.update(dict3)
print(dict2)