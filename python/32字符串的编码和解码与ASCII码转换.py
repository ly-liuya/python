#编码和解码
str1 = "我爱你中国"
# encode() 编码 gbk utf8
# print(str1.encode())
# b'\xe6\x88\x91\xe7\x88\xb1\xe4\xbd\xa0\xe4\xb8\xad\xe5\x9b\xbd'

# print(str1.encode('utf-8'))
# print(str1.encode('gbk'))

jbk1 = b'\xce\xd2\xb0\xae\xc4\xe3\xd6\xd0\xb9\xfa'
str2= b'\xe6\x88\x91\xe7\x88\xb1\xe4\xbd\xa0\xe4\xb8\xad\xe5\x9b\xbd'
# print(str2.decode())
# print(jbk1.decode('gbk'))
# print(str2.decode('utf-8'))

# ASCII 码的转换
# chr() 将对应的ASCII码转换为字符
print(chr(97))  # a
print(chr(68))  # D

# ord() 获取字符对应的ASCII 码的值
print(ord("c")) # 99
print(ord("Z")) # 90


