# 需求：在当前文件中，有10个地方需要输入1-10之间的所有的数字
"""
for i in range(1,11):
     print(i)
"""

# 上述遇到的问题：1、重复代码 2、程序的维护
# 可以使用函数来解决
# 函数：可以理解为，在项目中，经常使用的功能，将其程序提取出来，封装
# 一下，方便后续的调用和维护
"""
函数的语法：
   def 函数名(参数1，参数2，参数3....):
       函数体
    1、使用def关键字声明函数
    2、函数有两部分组成：声明部分和实现部分
    3、命名规则：要遵循标识符的命名规则，尽量做到见名知意
    4、函数定义时的参数，叫做形式参数（形参）可以写，也可以不写，取决于功能需求
    5、函数体要缩进
    6、函数要想使用，必须要条用，调用格式：函数名()
    7、函数调用必须在函数定义之后
"""
def test():
    for i in range(1, 11):
        if i % 2 == 1:
         print(i)


test()