# open()
"""
路径分为两种：
    1、绝对路径：从电脑的盘符开始的路径 比如：E:\PycharmProjects\python\demo.txt
    \ 表示转义字符
    E:/PycharmProjects/python/demo.txt
    2、相对路径：从当前执行文件所在的文件夹开始路径
        .表示当前目录(前执行文件所在的文件夹)  可以省略不写
        ..表示的是上次目录
        ../../ 表示上上级目录
"""
# 绝对路径演示
"""
# 打开文件
file = open("E:/PycharmProjects/python/jueduilj.txt",encoding="utf-8")
# 读取文件的内容
print(file.read())
# 关闭文件资源
file.close()
"""

# 相对路径演示
"""
file1 = open("hello.txt",encoding="utf-8")
print(file1.read())
file1.close()
"""

file2 = open("../测试/1.txt",encoding="utf-8")
print(file2.read())
file2.close()
