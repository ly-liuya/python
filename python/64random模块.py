# random 模块主要用于生成随机数或者从一个列表中随机获取数据
import  random
print(random.random())  # 随机生成0-1之间的浮点数
print(random.uniform(10,20))  # 生成指定范围内的随机浮点数
print(random.randint(10,30))  # 生成指定范围内的随机的整数
print(random.randrange(10,30,2))  #生成指定范围内的随机整数
print(random.choice("abcdefg"))  # 从指定内容中随机获取一个片段
print(random.sample("123abcdefg",3))  # 从指定内容中获取指定长度的数据
