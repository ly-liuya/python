# 1、字符串的声明：
#    使用单引号引起来
#    使用双引号引起来的字符串
#    使用三个单引号引起来的字符串
#    使用三个单引号引起来的字符串
s1 = 'Hello'
print (s1)

s2 = "World"
print (s2)

s3 = '''床前明月光
'''
print (s3)

s4 = """疑是地上霜
"""
print (s4)

#2、若字符串中的内容还需要引号包裹，外面是单引号，里面只能使用双引号；
# 外面若是双引号，里面只能使用单引号
n = "i say:'my name is aimi'"
m = 'i say:"my name is aimi"'
print(n)
print(m)

# 3、转义字符：
# 转义字符	描述
# \ (在行尾时)	续行符
# \\	反斜杠符号
# \'	单引号
# \"	双引号
# \a	响铃
# \b	退格(Backspace)
# \e	转义
# \000	空
# \n	换行
# \v	纵向制表符
# \t	横向制表符
# \r	回车
# \f	换页
# \oyy	八进制数，yy代表的字符，例如：\o12代表换行
# \xyy	十六进制数，yy代表的字符，例如：\x0a代表换行
# \other	其它的字符以普通格式输出
s6 = '\tHello\nWorld'
print (s6)

# 4、
"""
字符串前面加r,表示原样输出
字符串前面加f,表示支持{}语法
"""
h = r"i am a \teacher"
print(h)

name = "张三"
age = "18"
print(f"我的姓名是：{name},年龄是：{age}")





