# 封装、继承、多态
# 多态：一种事物的多种体现形式，函数的重写就是多态的一种体现
# 在面向对象中的多态，指的是父类的引用指向子类的对象

# 父类
class Animal():
    def eat(self):
        print("吃饭的方法")

# 子类
class Fish():
    def eat(self):
        print("大鱼吃小鱼，小鱼吃虾米")

class Dog():
    def eat(self):
        print("狼行千里吃肉，狗行千里吃粑粑")

class Cat():
    def eat(self):
        print("猫爱吃鱼")


# 严格意义多态的体现
class Person():
    def feed(self,animal):
        animal.eat()




# 最简单的多态体现
"""
   在父类和子类中出现了函数重名的情况，会调用子类的函数
子类和父类函数重名的情况就叫做多态
    不同的子类之间调用和父类方法名一样的方法，调用的都是自己的方法，这就是多态的一种体现
    


"""

fish = Fish()
dog = Dog()
cat = Cat()
fish.eat()
dog.eat()
cat.eat()

# 严格意义上多态的体现
Person().feed(fish)
