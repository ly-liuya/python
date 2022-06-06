#python3中有6个标准的数据类型
"""
----
Number 类型
String 类型
List 类型
Touple 类型
Dict 类型
Set 类型

"""

# Number 类型 主要包含 int(整型) float(浮点类型) bool类型
# int(整型)
num = 32
print(num)

# float(浮点类型)
num1 = 3.21
print(num1)
# bool类型 在python中归纳为int 类型的一个子类 值有2个 ，True(真) False(假)
bool1 = True
bool2 = False
print(bool1,bool2)
print(4<3) #False
print(11>8) #True

# String 类型  字符串类型主要有数字，字母，下划线，汉字，一般使用单引号或者双引号包裹文本内容
str1 = "hello"
str2 = 'world'
str3 = '''
床前明月光,
疑似地上霜,
举头望明月，
低头思故乡。
'''
print(str1,str2,str3)

# List 类型 列表使用[]表示，[]里面可以存放字符、数字、字符串、嵌套列表
list1 = ['古力娜扎','吴京','李晨']
print(list1)

# Touple 类型 元组使用()来表示，他是一种特殊的列表，()里面可以存放字符、数字、字符串、嵌套元组
tup = (12,43,9,87,True,False,"world")
print(tup)

# Dict 类型 字典使用{}来表示，字典由索引和对应的值组成{key1:value1,key2:value2.....}
user={"name":"吴京","age":18,"sex":"男"}
print(user)
# Set 类型 集合 使用{}来表示，{}里面直接存放值即可
set1 = {123,87.56,True,False}
print(set1)
