# 模块的本质就是一个python文件，我们根据自己项目的需求写的一些文件就是自定义模块

# 通过import 导入自定义模块
#第一种方式：导入自定义模块的方式
"""
import my_module
print(my_module.name)
my_module.test()
"""

# 第二种方式：导入自定义模块的方式 * 表示通配符，代表自定义模块中所有的变量以及方法
"""
from my_module import *
print(age)
test()
"""

# 第三种方式：
from my_module import name,age
print(name)
print(age)