# strip() 去除字符串两边的指定字符（默认去除的是空格）

str1 = " today is a nice day "
str2 ="***today is a nice day***"
print(str1)
print(str1.strip())
print(str2)
print(str2.strip("*"))

# lstrip() 只去除字符串左边的指令字符
print(str2.lstrip("*"))
# rstrip() 删除 string 字符串末尾的空格
print(str2.rstrip("*"))

# 字符串的分割和并
# split() 以指定字符对字符串进行分割(默认是空格)
str3 = "this is a string example..."
print(str3.split())
# ['this', 'is', 'a', 'string', 'example...']

print(str3.split("i"))
# ['th', 's ', 's a str', 'ng example...']

# join() 合并字符串
str4 ="_"
tup =("hello","every","body")
print(tup)
print(str4.join(tup))  # hello_every_body



