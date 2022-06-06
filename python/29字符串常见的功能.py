# 1、获取字符串的长度和字符串出现的次数

str1 = "我的电脑有点卡了，你的电脑卡吗？"
# len()字符串的长度
print(len(str1))  # 16
# count() 统计字符串出现的次数
print(str1.count("电脑"))  #2

# 2、字符串的大小写转换，
# upper():将小写字母转换为大写字母
# lower()：将大写字母转换为小写字母
str2 = "i miss you VERY much"
print(str2.upper())
print(str2.lower())

# swapcase:将字符串中的大写字母转为小写，将小写转为大写
print(str2.swapcase())

# title(): 将单词的首字母转换为大写
print(str2.title())

# 3、查找字符串出现的位置
str3 = "abcdefghijklmn1239876l54zxyslt"
# find() 查找子串在字符串中第一次出现的位置，若找到了返回的是下标，
#  若未找到，返回的是-1
print(str3.find("l"))  # 11
print(str3.find("o"))  #-1

# index(),跟find()方法一样，只不过如果str不在 string中会报一个异常.
# 找到就返回下标，没找到就报错
print(str3.index("a"))  # 0
# print(str3.index("p")) #直接报错

# rfind() 查找子串在字符串中最后一次出现的位置,找到了返回的是下标
# 若未找到，返回的是-1
print(str3.rfind("l"))
print(str3.rfind("q")) # -1
# rindex() 查找子串在字符串中最后一次出现的位置,找到了返回的是下标
# 若未找到，报错
print(str3.rindex("l"))
# print(str3.rindex("q"))

# 在指定范围内查找
print(str3.find("l",3,12))
print(str3.index("l",3,12))
print(str3.rfind("l",12,30))
print(str3.rindex("l",12,30))