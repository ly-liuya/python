# 1、输出1-100之间所有的数字
"""
num = 1
while num <=100:
    print(num)
    num += 1
"""

# 2、输出1-100之间所有数字的和
"""
num = 1
result = 0 #定义变量，接收1-100之间的和
while num <= 100:
    result = result + num
    num += 1
print(result)
"""

# 3、计算1-100之间所有的偶数的和
"""
num = 1
result = 0 #定义变量，接收所有偶数的和
while num <= 100 :
    if num % 2 == 0: # 判断数字是否为偶数
        result = result +num
    num +=1
print(result)
"""

# 4、计算1-100之间所有的奇数的和
num = 1
result = 0 #定义变量，接收所有奇数的和
while num <= 100 :
    if num % 2 != 0: # 判断数字是否为奇数
        result = result +num
    num +=1
print(result)


