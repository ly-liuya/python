# 匹配多个字符
"""
1、? : 表示前面的字符可以出现0次或者1次
2、+ : 表示前面的字符可以出现1次或者多次
3、* ：表示前面的字符可以出现0次或者多次

{}: 表示前面的字符可以出现指定的次数的范围
{3} :表示前面的字符只能出现3次
{3,6}:表示前面的字符能出现3-6次
{3,}:表示前面的字符至少出现3次
{,3}:表示前面的字符最多出现3次
"""
import re
# 1、?
print(re.search("goog?le","goole"))  # <re.Match object; span=(0, 5), match='goole'>  0次情况
print(re.search("goog?le","google"))  # <re.Match object; span=(0, 6), match='google'>  1次情况

print(re.search("goog?le","googgggle")) # None  多次的情况
print("---?-----")

# 2、+

print(re.search("goog+le","goole"))  # None
print(re.search("goog+le","google"))  # <re.Match object; span=(0, 6), match='google'> 出现1次
print(re.search("goog+le","googgle"))  # <re.Match object; span=(0, 7), match='googgle'> 出现多次
print("---+-----")


print(re.search("goog*le","goole"))  # <re.Match object; span=(0, 5), match='goole'> 出现0次
print(re.search("goog*le","googgggle"))  #  <re.Match object; span=(0, 9), match='googgggle'>  多次的情况

print("---*-----")


print(re.search("goog{3}le","googggle"))  # <re.Match object; span=(0, 8), match='googggle'>
print(re.search("goog{3}le","google"))  # None

print(re.search("goog{3,6}le","googggle"))  #  <re.Match object; span=(0, 8), match='googggle'>
print(re.search("goog{3,6}le","googgggle"))  # <re.Match object; span=(0, 9), match='googgggle'>
print(re.search("goog{3,6}le","googggggggggle"))  # None

print(re.search("goog{3,}le","googggggggle"))  #  <re.Match object; span=(0, 12), match='googggggggle'>
print(re.search("goog{,3}le","googgle"))  # <re.Match object; span=(0, 7), match='googgle'>
