# 面向对象的三大特性：封装  继承 多态
"""
封装：
    函数的定义，类的定义，里面包含了属性和方法
继承：
    将一些类公共的属性和方法提取出来，放到一个专门的父类中去，其他的子类直接继承这个父类后就可以直接使用这些属性和方法
多态：
    更多的体现在解决一些特殊问题时候的技巧

"""


class Person():
    def say(self):
        print("说话的方法")


class Boy(Person):  # 在子类中继承父类只需要在定义子类时，参数列表写上父类的名称即可
    def eat(self):
        print("吃饭的方法")


xiaoming = Boy()
xiaoming.eat()  # 对象直接调用子类的方法
xiaoming.say()  # 对象调用父类的方法


# 有构造函数的继承
class Animal():
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def run(self):
        print("我是跑的方法")


class Dog(Animal):
    def __init__(self,name,sex,weight): #现在子类的构造函数中继承父类的属性，然后在重构
# 1、继承父类的构造方法
#         Animal.__init__(self,name,sex)
# 2、隐式继承父类的构造函数
        super(Dog, self).__init__(name, sex)
# 定义自己类的属性
        self.weight = weight



    def wang(self):
        print("汪汪")

taidi = Dog("泰迪","公","5000")
taidi.wang()
taidi.run()
print(taidi.name)
print(taidi.sex)