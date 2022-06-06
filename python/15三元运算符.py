# 三元运算符,是对if else 的简化

# if else 的写法
a = 12
b = 54

if a>b:
    print("大的数字是"+ str(a))
else:
    print("大的数字是"+ str(b))

#三元运算符的写法
max = a  if a >  b else b
print(max)