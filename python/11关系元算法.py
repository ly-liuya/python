# 运算符	 描述	                         范例
# ==	等于 - 比较对象是否相等	        (a == b) 返回 False
# !=	不等于 - 比较两个对象是否不相等	    (a != b) 返回 true.
# <>	不等于 - 比较两个对象是否不相等	    (a <> b) 返回 true。类似 !=
# >	大于 - 返回 x 是否大于y	            (a > b) 返回 True
# <	小于 - 返回 x 是否小于y	            (a < b) 返回 False
# >=	大于等于 - 返回 x 是否大于等于 y	(a >= b) 返回 True
# <=	小于等于 - 返回 x 是否小于等于 y	(a <= b) 返回 False

a = 10
b = 2
c = 0

if ( a == b ):
   print ("1 - a 等于 b")
else:
   print ("1 - a 不等于 b")

if ( a != b ):
   print ("2 - a 不等于 b")
else:
   print ("2 - a 等于 b")


if ( a < b ):
   print ("4 - a 小于 b")
else:
   print ("4 - a 大于等于 b")

if ( a > b ):
   print ("5 - a 大于 b")
else:
   print ("5 - a 小于等于 b")

# 修改变量 a 和 b 的值
a = 5
b = 20
if ( a <= b ):
   print ("6 - a 小于等于 b")
else:
   print ("6 - a 大于  b")

if ( b >= a ):
   print ("7 - b 大于等于 a")
else:
   print ("7 - b 小于 a")