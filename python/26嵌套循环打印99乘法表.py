#1、总结：嵌套循环中，外层循环执行一次，内层循环执行一圈
#a.使用while循环打印9*9乘法表
i = 0  # 控制外层循环
while i < 9:
    i += 1
    j = 0 # 内层循环
    while j < i: #每行显示几个乘法，取决于第几行
        j +=1
        print(i,"*",j,"=",i*j,end=" ")
    print()

#b.使用for循环打印9*9乘法表
for a in range(1,10):
    for b in range(1,a+1):
        print(a,"*",b,"=",a*b,end=" ")
    print()

