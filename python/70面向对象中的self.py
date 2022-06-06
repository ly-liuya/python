# self关键字
class Student:
    def eat(self):
        print(self)

stu = Student()
stu.eat()     # 此时self 表示的是stu这个对象

stu1 = Student()
stu1.eat()    # 此时的self 表示的是stu1这个对象