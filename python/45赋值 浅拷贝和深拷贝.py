# 赋值：其实就是对象的引用（别名）
# list1 = [12,31,4,5565,34]
# list2 = list1
# print(list1)
# print(list2)
#
# list1[2] = "哈哈"
# print(list1)
# print(list2)

#如何解决上述的问题，可以使用浅拷贝的方式
# 可以解决一维列表复制的问题
import  copy
list3 =[23,45,6,78,93,42]
list4 = list3.copy()
# print(list3,list4)
list3[3] = "呵呵"
# print(list3,list4)

# 深拷贝：用来解决多维列表修改元素时，不能独立处理的问题
list5 = [23,43,[45,52,47],98,94]
# 深拷贝的用法 ：list2 =copy.deepcopy(list1)
list6 = copy.deepcopy(list5)
print(list5)
print(list6)
list5[2][1] = "张三"
print(list5)
print(list6)