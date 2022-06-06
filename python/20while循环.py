# 输出10遍的Helloworld
#循环：主要用于解决实现相同的事情重复做
#python中的循环分为 while 和 for 循环
"""
while 循环的语法：
1、初始条件
while 2.判断条件：
    循环体
    3、更新条件
注意：
a.在while 循环中，初始条件只会在第一次循环的时候执行，后续的循环不在执行初始条件
b.在python中，不支持，自增，自减， ++ --
C.在python中没有 do while 循环
"""
count = 0
while count < 10:
    print("hello world!")
    count += 1


