# 类方法：使用 @classmethods 装饰器修饰的方法叫做类方法，可以通过类名调用可以通过对象使用
# 一般情况下下使用类名调用
class Animal():
    # 类属性
    name = "动物类"

    def __init__(self, name):
        self.name = name

    @classmethod
    def run(cls):
        print("我是类方法")
        print(cls)
        print(cls == Animal)  # cls表示当前类 True
        print(cls.name)

    @staticmethod
    def eat():
        print("我是静态方法")


# Animal.run()  # 通过类名调用类方法
dog = Animal("中华土狗")
# dog.run()   # 对象调用类方法

Animal.eat()  # 通过类名调用静态方法
dog.eat()   # 对象调用静态方法
"""
总结：
    类方法：
        1、通过@classmethod装饰器修饰的方法叫做类方法
        2、类方法可以使用类名调用(推荐) 对象可也可以调用
        3、没有self,在类方法中不可以使用其他对象的属性和方法（包括私有属性和方法）
        4、可以调用类属性和其他的类方法
        5、类方法中的cls，是class的简写，可以更换为其他的，一般使用cls来表示当前类
        6、cls 表示的是当前类
        
    静态方法：
        1、通过@staticmethod装饰器修饰的方法叫做静态方法
        2、通过类名调用静态方法（推荐） 对象也可以调用静态方法
        3、静态方法中的形参中没有cls,单静态方法中不建议使用（类属性\类的方法\静态方法）
        4、静态方法一般是一个单独的方法，只是写在类中
        
        
"""
