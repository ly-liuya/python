#
# 类
class Person:
    # 属性：一般用来描述静态信息
    name = "张三"
    sex = "男"

    def eat(self):
        print("吃饭的方法")

    def say(self):
        print("我是说话的方法")


p = Person()
# 通过对象访问类中的属性
print(p.name)
# 通过对象访问类中的方法
p.say()
