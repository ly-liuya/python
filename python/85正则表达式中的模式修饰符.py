# 模式修饰符: 主要用来修饰我们写的正则表达式，是一个可选参数
# .	匹配任意字符，出了换行符   \n 表示换行符
# re.S:可以使正则表达式中的 . 匹配到换行符
# re.I: 忽略大小写

import re
print(re.search("shenzen.","shenzen9"))  # <re.Match object; span=(0, 8), match='shenzen9'>

print(re.search("shenzen.","shenzen\n"))  #  None

print(re.search("shenzen.","shenzen\n",re.S))  # <re.Match object; span=(0, 8), match='shenzen\n'>

print(re.search("shenzen[a-z]","shenzenM"))   # None

print(re.search("shenzen[a-z]","shenzenM",re.I))  #  <re.Match object; span=(0, 8), match='shenzenM'>
