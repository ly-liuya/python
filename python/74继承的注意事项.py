# 定义一个类
class Person(object):
    def __init__(self, name):
        self.name = name

    def run(self):
        print("跑步的方法")


"""
注意：
    1、objects 是所有类的父类，如果一个类没有显示指名他的父类，则默认为object（可以省略不写）
    2、python 中的面向对象可以实现多继承
"""

person = Person("张三")
# person.run()
# print(person.name)


# 多继承语法：
"""    
class 子类类名(父类1,父类2,父类3....)
    属性
    方法

"""


# 定义一个父亲类
class Father():
    def __init__(self, surname):
        self.surname = surname

    def make_money(self):
        print("钱难挣！")

# 定义一个母亲类
class Mother():
    def __init__(self,height):
        self.height = height

    def eat(self):
        print("一言不合就干饭")

# 定义子类
class Son(Father,Mother): #子类继承多个父类时需要把父类的名称写在参数列表中即可，用,隔开
    def __init__(self,surname,height,weight):
        # 继承父类构造函数
        Father.__init__(self,surname)
        Mother.__init__(self,height)
        self.weight = weight

    def say(self):
        print("我很好")


son = Son("李四","178","120")
print(son.surname)
print(son.height)
son.say()
son.make_money()