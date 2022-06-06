# 定义一个类
class Person(object):
    def __init__(self, name):
        self.name = name

    def run(self):
        print("跑步的方法")


"""
注意：
    1、objects 是所有类的父类，如果一个类没有显示指名他的父类，则默认为object

"""

person = Person("张三")
person.run()
print(person.name)
