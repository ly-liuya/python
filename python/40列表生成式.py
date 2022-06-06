# 1、生成 1-10 之间所有的整数
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = list(range(1,11))
print(list2)

# 2、通过程序的方式得到下列列表[1,4,9,16,25]
# 第一种方式：使用原始方式生成
list3 =[]
for i in range(1,6):
    list3.append(i ** 2)
print(list3)

# 第二种方式：使用列表生成式
list4 = [i ** 2for i in range(1,6)]
print(list4)

# 练习：使用列表生产式，生成1-10之间所有的奇数
list5 = [i for i in range(1,11) if i % 2 ==1]
print(list5)

# 练习：使用列表生产式，生成1-10之间所有的奇数且能被3整除
list6 =[i  for i in range(1,11) if i % 2 == 1 and i % 3 == 0]
print(list6)