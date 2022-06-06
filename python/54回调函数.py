def test():
    print("hello world")

# test()

# demo = test()  #当把函数名赋值给一个变量的时候，那这个变量就实现了和函数一样的功能
# demo

# 回调函数：把一个函数（a） 作为一个参数传递到另外一个函数（b）中去,那么这个函数a我们就叫做回调函数
def add(x,y):
    print(x+y)
def cha(a,b):
    print(a-b)
def ji(c,d):
    print(c*d)
def shang(e,f):
    print(e/f)

# add(12,34)
# cha(76,31)

# 需求：封装一个万能函数，传入两个参数，直接实现加减乘除的操作
def demo(x,y,func):
    func(x,y)

demo(12,23,add)

demo(87,42,cha)