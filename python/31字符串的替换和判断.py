# 1、替换：将字符串中指定的内容进行替换
"""
replace() 对字符串中的指定数据进行替换
    第一个参数：要替换的内容
    第二个参数：替换后的内容
    第三个参数：控制替换的次数


"""
str1 = "这个店铺的商品是垃圾，这么垃圾的商品怎么能用来卖呢？"
# print(str1)
# print(str1.replace("垃圾","**"))
# print(str1.replace("垃圾","**",1))

# 判断：返回结果是布尔类型，若成立返回True,不成立返回Fslse
# isupper() 检测字符串中的字母是否全部是大写
print("helloWORLD".isupper())  #  False
print("HELLO".isupper())  #True

# islower() 检测字符串中的字母全部是小写
print("hello".islower()) #True
print("Hello".islower()) #False

# isdigit() 检测字符串是否全部是数据
print("121212".isdigit()) #True
print("1212AS".isdigit()) #False

# istitle() 检测字符串中的首字母是否全部是大写
print("Hello World".istitle()) #True
print("hello World".istitle()) #False

# isalpha() 检测字符串中的内容是否全部是由字母或者文字组合
print("你好Jack".isalpha()) #True
print("你好Jack123".isalpha()) #False
