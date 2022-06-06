# 下标：也叫做索引，表示第几个数据
#在计算机程序中，下标一般从0开始，可以通过下标获取指定位置的数据

str1 = "welcome"
print(str1[3]) #c

#切片：从字符串中复制一段指定的内容，生成一个新的字符串
str2 = "welcome to xinjiang"
print(str2[0:3])  # wel 包含star 不包含end
print(str2[1:])  # 若只设置了star ，表示只有开始下标，一直截取到最后
print(str2[:4]) # 若只设置了end,表示从第一个字符开始，到截取到end
print(str2[1:4:2]) #ec
# print(str2[1:4:0])  #步长不可以设置为0
print(str2[::]) #表示复制字符串
print(str2[::-1]) #表示反转字符串
print(str2[-9:-3]) #表示从后面往前面数
"""
切片语法：
    字符串[start:end:step]
        start:开始下标，截取的字符串包含开始下标的数据
        end:结束下标，截取的字符串不包含结束下标的数据
        step：表示步长 默认是1
"""