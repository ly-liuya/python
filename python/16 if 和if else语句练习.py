#1、任意输入一个数字，判断是否大于16 ，若大于16输出该数字大于是6，否则不输出

""""
num1 = int(input("请输入一个数字："))
if( num1  >  16):
    print("您输入的数字是大于16的数字：" + str(num1))
"""
#2、任意输入一个数字，判断是奇数还是偶数
"""
num1 = int(input("请输入任意一个数字:"))
if num1 % 2 == 0:
    print(str(num1) + "是偶数")
else :
    print(str(num1) + "是奇数")
"""

#3、分别输入年月日 ，三个日期，判断输入的日是这一年中的第几天（
# 要考虑闰年和平年的情况）

year = int(input("年："))
month = int(input("月："))
day = int(input("日："))
# 定义变量，表示是一年中的第几天
days = day
if month > 1 :
    days += 31
if month > 2 :
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 :
        days += 29
    else : days+=28
if month > 3:
    days += 31
if month > 4:
    days += 30
if month > 5:
    days += 31
if month > 6:
    days += 30
if month > 7:
    days += 31
if month > 8:
    days += 31
if month > 9:
    days += 30
if month > 10:
    days += 31
if month > 11:
    days += 30
print("在"+str(year)+"的第" +str(days) + "天")



