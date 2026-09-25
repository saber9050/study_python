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