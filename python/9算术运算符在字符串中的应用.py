# 算术运算符应用在两个字符串之间，会把两个字符串拼接成一个字符串
str1 = "hello"
str2 = " world"
print(str1+str2)

# 注意：在python中数字和字符串不能进行加法运算
str3 = "welcom"
num = 12
print(str3 + num) # 数字和字符串不能进行加法运算
print(str3+ str(num))