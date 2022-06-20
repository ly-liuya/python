"""
\d :匹配的数字：0-9之间任意的数字， 等同于[0-9]
[0-9]

\D:匹配非数字字符，可以理解为对\d 取反  [^0-9]
[^0-9] 表示匹配所有的非数字字符

\w: 表示匹配字母数字及下划线 [0-9a-zA-Z_]

\W: 表示匹配非字母数字及下划线 [^0-9a-zA-Z_]

\s	匹配任意空白字符，等价于 [\r\n\t\f] (空格、回车、换行，制表符，换页)
\S	匹配任意非空字符,等价于 [^\r\n\t\f]




"""
import re
# print(re.search("he\dllo","he8llo"))  # <re.Match object; span=(0, 6), match='he8llo'>
# print(re.search("he[0-9]llo","he8llo"))  # <re.Match object; span=(0, 6), match='he8llo'>
# print(re.search("he\dllo","heallo"))  # None

print(re.search("hello\D","hello1"))  # None
print(re.search("hello\D","hello_"))  # <re.Match object; span=(0, 6), match='hello_'>
print(re.search("hello\D","helloS"))  # <re.Match object; span=(0, 6), match='helloS'>
