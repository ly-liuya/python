# 1、合并列表，通过 + 实现

list1 = [12,445,6,4.53]
list2 = ['东皇太一','貂蝉','张飞','吕布']
print(list1 + list2)

# 2、判断指定元素是否在列表中，通过成员运算符 in 或者 not in 进行判断，返回值是一个布尔类型
list3 = ['hello','world','你好','呵呵',124,56]
# print("呵呵" in list3)  # True
# print("哈哈" in list3)  # False
if "hello" in list3 :
    print("字符串在列表中")
else:
    print("不在列表中")


# 3、列表的切片
print(list3[1:4])
print(list3[1:])
print(list3[:3])
print(list3[:])
print(list3[-3:])


