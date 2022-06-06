#数据类型转换 int====>str  str====>int  bool===>int
#不同的数据类型，运算规则不一样

# age = int(input("输入年龄："))
# print(age)  #str
#在python中，字符串和整型不能直接进行数字运算
# print(age + 1)

#int() 将其他数据类型转换为整型
'''
参数：
 1、要转换的数据类型
 2、base = 10 表示进制，默认是10进制
 返回值：
 返回的是一个整型的数字
'''

# str = "hello"
# num = int(str) #报错
# print(num)

num1 = "32"
num2 = int(num1)
print(num2)
# print(type(num1),type(num2))

str1 = 12
# print(int(str1))#12
# print(int(str1,base=16))#18 表示将字符串12以16进制的形式转换为整型


#str():将其他数据类型转换为字符串类型
num3 = 12
num4  = 87
print(num3+num4)
# print(type(num3+num4)) #<class 'int'>

str1 = str(num3)
str2 = str(num4)
#print(type(str1)) #<class 'str'>
#print(type(str2)) #<class 'str'>

# print(str1+str2) #1287 拼接

#float() :将其他数据类型转换为浮点型
float1 = "12.34"
# print(type(float1))  #<class 'int'>
# print(type(float(float1))) #<class 'float'>
float2 = "hello123" #不能转换为浮点型
#print(float(float2)) #报错


#布尔类型：True 和 False
# bool():将其他数据类型转换为布尔类型
print(bool(100))  # True
print(bool(3.12))  # True
print(bool(0))  # False
print(bool("hello"))  # True
print(bool(''))  # False
print(bool(""))  # False
print(bool(' '))  # True
print(bool([12,34,7]))  # True
print(bool([]))  # False
print(bool((32,45,67)))  # True
print(bool({"name":"张三"}))  # True
print(bool(()))  # false
print(bool({}))  # false
print(bool(None))

#数字0 ，空字符串""或者空'',空列表[],空元祖(),空字典{}，空集合set(),None
#这些数据转换为bool类型时是False

#隐式类型转换 一般用于条件表达式
print(3 > 2)   #  True
print(98 < 87)  # False
numB = 12
if numB: # numB在这里隐式转换为True
    print("numB是一个数字")

# list():将其他数据类型转换为列表
tup = (12,34,678,9)
print(tup)
print(type(tup)) #<class 'tuple'>
print(list(tup))
print(type(list(tup))) #<class 'list'>

list1 = list(tup)
print(list1)
print(list1) #[12, 34, 678, 9]

strL = "hello"
list2 = list(strL)
print(list2) # ['h', 'e', 'l', 'l', 'o']

numL = 21  # 报错
#print(list(numL))
# 注意：一般情况下，是字符串和元组类型的数据转换为列表数据类型


#tuple() 将其他数据类型转换为元组

list3 = [12.45,678,9,True,False,87]
print(type(list3))  #  list
print(type(tuple(list3)))  #<class 'tuple'>

string1 = "123"
print(type(string1)) # str
print(type(tuple(string1))) #tuple
print(tuple(string1)) #('1', '2', '3')



