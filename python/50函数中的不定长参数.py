# 不定长参数：
# 1、 *args:用来接收多个位置参数，得到的是一个元组
# 2、 **kwargs:用来接收多个关键字参数，得到的是一个字典，在传输参数的时候
# 必须是key=value的形式传输
def demo(*args):
    print(args)

# demo("hello",12,34,5,65)
# demo(43,45,6)

# 在定义函数时，若函数中有多个参数，其中某一个参数是不定长参数，
# 一般把不定长参数放在参数列表的最后面
def test(name,*args):
    print(name,args)

test("貂蝉",12,24,56,86,43,"hello")

def fn(**kwargs):
    print(kwargs)

fn(x=12,y=34,z=43)