# 什么是设计模式？
"""
经过多次的实验，总结出来解决一些特殊问题的方案，叫做设计模式
常见的设计模式有23种：
比如：单例设计模式\工厂设计模式\门面设计模式\代理设计模式\装饰设计模式等等

"""

# 单例设计模式
"""
单例：单个实例对象，在程序运行的过程中，确保某一个类只能有一个实例【对象】，
    不管在那个模块中获取对象，获取到的都是同一个对象
"""


# 应用场景：数据库的连接操作
# 实现
class Person():
    def __init__(self, name):
        self.name = name

    # 创建一个类属性，接收创建的对象
    instance = None
    @classmethod
    def __new__(cls, *args, **kwargs):
        print("__new__")
        if cls.instance == None:
            cls.instance = super().__new__(cls)
        return  cls.instance

p1 = Person("陈梦")
p2 = Person("张三")
p3 = Person("李四")
print(p1 == p2 == p3)