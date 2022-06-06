# 标识符主要作为变量\函数\类\模块以及其他对象的名称
# 定义合法标识符的规则：
#     1、由数字 字母 下划线组成 并且不能以数字开头
#     2、严格区分大小写 age 和Age 是两个不同的标识符
#     3、不能使用python中的关键字作为标识符，可以通过keyword模块中的kwlist属性查看有哪些关键字
#     python 中常见的关键字：
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async',
# 'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
# 'else', 'except', 'finally', 'for', 'from', 'global',
# 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not',
# 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# import keyword
# print(keyword.kwlist)

# 定义标识符的命名规范：
# 1、见名知意
# 2、遵守一定的命名规范
#     2.1小驼峰命名法：第一个单词首字母小写，以后的每个单词的首字母大写 例如：userNameAndPassword
#     2.2大驼峰命名法：每个单词的首字母大写，例如：UserName
#     2.3下划线命名法：每个单词使用下划线进行拼接，例如：user_name_and_password
# 注意：一般情况下，在python中的变量 函数 模块使用下划线命名法
# 类名一般使用大驼峰命名法

name1 = "jack"
# 12name= "hello" 标识符命名不能以数字开头
# def="函数" 标识符命名不能舒勇关键字
print(name1)
# print(12name)

