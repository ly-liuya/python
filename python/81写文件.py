# open() 打开指定路径的文件

"""
注意：
    1、若打开的文件路径不存在，则直接创建一个新文件
    2、mode = "w" 会把原文件中的内容全部替换
    3、mode =  "a" 追加的方式向文件中写入内容，不会影响原文件的内容

"""
# file = open("cc.txt","w",encoding="utf-8")
file = open("cc.txt","a",encoding="utf-8")

# write
file.write("追加内容")
# flush() 刷新管道
file.flush()
file.close()