import os
# 主要用于获取系统的功能，操作文件或者文件夹
print(os.curdir)  # .当前目录
# getcwd() 获取当前路径
print(os.getcwd())  # 获取当前路径

# mkdir() 创建文件夹，（不能创建已经存在的文件夹）
# os.mkdir("测试")
# rmdir() 删除文件夹（只能删除空文件夹）
# os.rmdir("测试")

# rename() 重命名文件或文件夹
# os.rename("测试","演示")

# remove() 删除文件
# os.remove("64demo.py")

# 拼接路径os.path.join()
# os.path.join(r"路径")

#os.path.getsize()
print(os.path.getsize("hello.py"))

# 判断是否是文件 os.path.isfile() 若是返回true，若不是返回false
print(os.path.isfile("hello.py"))  # true

# 判断是否是文件夹
