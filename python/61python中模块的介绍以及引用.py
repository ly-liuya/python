# 模块，一个py文件可以简单的理解为一个模块
# 并不是所有的py文件都可以导入使用
# 如果我们希望py文件能够被当做模块一样到日使用，必须遵循命名规则
# python为了方便我们快速开发，提供了很多内置模块
# 常见的内置模块
# os sys math random datetime time calendar hashlib uuid hmac

# 第一种：直接使用import 关键字导入模块
import time
# 导入了这个模块以后，可以使用该模块下所有的方法和变量
print(time.time())

# 第二种：from 模块名 import 方法名或者变量名
from random import  randint
print(randint(1,9))

# 第三种：from 模块名 import * 此处的 * 表示该模块下面所有的方法和变量名

# 第四种： import as 别名  as表示其别名
import datetime as dt
print(dt.MAXYEAR)

# 第五种：from 模块名 import 方法名或者变量名 as 别名
from copy import deepcopy as dp
print(dp("1111"))