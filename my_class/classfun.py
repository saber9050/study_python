"""
是类方法（或属性）还是实例方法，是看它是给类用还是实例用
"""

# 类方法
class Dog:
    name = "大黄"
    def __init__(self,age):
        self.age = age
    # 使用@classmethod装饰的方法是  类方法
    # 类方法通常实现与类相关的逻辑，例如操作类的信息，一些工厂方法
    @classmethod
    def run(cls,u):
        print("test1")

    # 工厂方法
    @classmethod
    def new(cls,age):
        return Dog(age)

    # 静态方法：使用@staticmethod装饰的方法， 通常用类来调用
    # 通常用于定义与类相关的工具方法
    @staticmethod
    def is_adult(age):
        if age > 18:
            print("成年")
        else:
            print("未成年")
# 用类调用类方法
Dog.run(3)

d1 = Dog
print(Dog.name)
# 修改类属性，其他实例也会同步修改
Dog.name = 888
print(Dog.name)
print(d1.name)

a = Dog.new(99)
print(a.__dict__)

a.is_adult(9)