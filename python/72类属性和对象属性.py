class Fish():
    # 类属性
    name = "鱼类"

    # 构造函数
    def __init__(self,weight):
        self.weight = weight
    def swim(self):
        print("游泳的方法")

# 创建对象
jinyu = Fish(234)
liyu = Fish(876)

# 访问类属性,对象和类都可以访问类属性
# print(Fish.name)  # 鱼类
# print(jinyu.name)  # 鱼类
# print(liyu.name)   # 鱼类

# 访问对象的属性,对象可以访问对象的属性，但是类不能访问对象的属性
print(jinyu.weight)
print(liyu.weight)
# print(Fish.weight)  # 报错


"""
总结：
    1、类属性可以使用类名访问（推荐） 对象也可以访问类属性（不推荐）
    2、对象的属性可以使用对象访问（推荐） 类不可以访问对象的属性
"""
# 修改类属性
Fish.name = "鲨鱼"
print(Fish.name)

jinyu.name = "金鱼"
print(jinyu.name)  # 金鱼 通过对象修改类属性时，只是动态的给当前对象添加了一个属性，并不能修改类属性

print(liyu.name)  # 鲨鱼  其他对象访问类属性时，还是原来的结果

# 修改对象的属性
jinyu.weight = "1斤"
Fish.weight = "500g"
print(jinyu.weight)
print(Fish.weight) # 500g
"""
总结：
    1、类可以修改类的属性（推荐） 通过对象修改类的属性的时候，只是动态的给当前对象添加一个属性。
    并没有修改类的属性，其他对象访问类属性值还是原来的值
    2、对象可以修改对象的属性（推荐） 类也可以修改对象的属性
    
"""
