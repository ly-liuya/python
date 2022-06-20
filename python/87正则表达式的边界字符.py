# 边界字符
"""
1、^ :行首匹配，以指定字符开头
2、$ :行位匹配，以指定字符结尾

^文本$ : 完全匹配


"""
# 转义字符 \ : 使正则表达式中的符号失去原有的意义
# \. : 表示一个普通的点 就不代表除了换行以外的任意字符了

import re
print(re.search("^world","world"))
# <re.Match object; span=(0, 5), match='world'>
print(re.search("^world","12world"))  #  None


print(re.search("world$","world"))
# <re.Match object; span=(0, 5), match='world'>

print(re.search("world$","world12"))  # None

print(re.search("^world$","world"))
# <re.Match object; span=(0, 5), match='world'>

print(re.search("^world$","worldworld"))  # None

print(re.search("wor\.ld","wor.ld"))
# <re.Match object; span=(0, 6), match='wor.ld'>