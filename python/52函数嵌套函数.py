# 函数之间是可以相互嵌套

def test():
    test1()
    print(111)

def test1():
    test2()
    print(222)

def test2():
    test3()
    print(333)

def test3():
    print(444)

test()
