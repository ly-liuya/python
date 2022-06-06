#print() 函数主要是将程序运行的结果显示出来，至于什么是函数，后续会进行详细的讲解
print()

"""
def print(self, *args, sep=' ', end='\n', file=None):  # known special case of print
        表示类名，一般指当前类
        表示可变参数，可以多个，一般表示我们要输出的数据
        表示输出多个数据时，多个数据之间的间隔，默认是空格
        表示print()函数执行完毕后，以什么结尾， 默认是换行
        表示文件名称 默认值是none（空）
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
    """

num = 123
num1 = 3.14
name = "吴京"
print(num,end="______")
print(num1,name)