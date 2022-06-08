# 类中任何方和属性，如果以两个下划线开头 ( __ ) 即为类的私有属性和私有方法
#
# 私有属性和私有方法只能在类的内部调用 ，不能在类的外部调用

class Girl():
    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        # 年龄设置为私有属性
        self.__age = age

    def say(self):
        print("说话的方法")
    # 私有方法
    def __kiss(self):
        print("吻别")

    def love(self,relationship):
        if  relationship == "情侣":
            self.__kiss()
        else:
            print("不能随便轻吻！!!")

    # 类的内部定义一个方法，可以访问私有属性
    def sayAge(self,boyFriend):
        if boyFriend == "小明":
            print(f"{self.name}偷偷的告诉{boyFriend}说：今年18岁了")
        else:
            print("保密")

hong = Girl("小红","女",18)
print(hong.name)
print(hong.sex)

# 在类的外部不能直接访问对象的私有属性。
# print(hong.age)
hong.say()
hong.sayAge("小凉")
hong.sayAge("小明")
# hong.__kiss()
hong.love("情侣")
hong.love("朋友")

"""
总结：
私有属性：
    1、格式：在属性之前加__ 比如：__age
    2、用法：只能在类的内部访问，不能再外部访问；可以在类的内部设置一个对外
        开放的接口，这个接口一般会设置各种条件判断满足后才可以访问，主要用于私密信息

私有方法：
    1、格式：在方法前加__ 比如：__kiss()
    2、用法：只能在类的内部访问，不能在类的外部访问，
        私有方法一般用于在类的内部实现某些功能，对外部来说没有实质意义
    

"""