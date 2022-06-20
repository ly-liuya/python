# open() 用于打开文件
"""
参数接收：
第一个参数：file 表示文件的路径
第二个参数：mode 表示打开文件时的模式，默认模式是：r（read）,w(write),a(append),
第三个参数：encoding 表示编码格式

返回值：
    打开后的文件对象

"""

file = open('demo.txt',encoding="utf-8")
print(type(file))
#读取文件中的内容
"""
在windows 系统中，打开文件模式是以gbk编码的方式打开文件
demo.txt 是utf-8
解决方案：读取和写入的格式要一致

"""
print(file.read())


# 文件内容读取完毕后，关闭文件资源
file.close()