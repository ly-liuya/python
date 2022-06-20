# 需求，判断用户输入的手机号码是否合法？
"""
def checkPhone(phone):
    if len(phone) != 11:
        print("手机号码长度不是11位")
        return
    if phone[0] != "1":
        print("手机号格式错误,不是1开头的")
        return
    if not phone.isdigit():
        print("手机号码不是全部是数字")
        return
    print("该手机号码是正确的手机号码")

checkPhone("11223344789")
"""

# 使用正则表达式验证手机号码

import re

result = re.search("^1\d{10}$", "18703022425")
if result:
    print("手机号码正确")
else:
    print("手机号码不合法")
