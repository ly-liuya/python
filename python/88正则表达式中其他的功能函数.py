#

import re

# 拆分 ： re.split(正则表达式，"要处理的数据")
print(re.split("\d","hello123world98everyone"))
# ['hello', '', '', 'world', '', 'everyone']

# 替换；re.sub(正则表达式，替换后的内容，要替换的字符)
str1 = " 今天   天气好晴朗  处处  好风光"
print(re.sub("\s+","...",str1))
# ...今天...天气好晴朗...处处...好风光

# 匹配中文：
chinese = "[\u4e00-\u9fa5+]+"
print(re.search(chinese,"hello 光头强 world 12"))
# <re.Match object; span=(6, 9), match='光头强'>
