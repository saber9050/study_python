"""
object类：

    1. 所有类都继承了 object 类
    2. 由于object类时所有类的父类，所以python中所有对象，都间接时object类的实例
    3. 所有对象都继承了object类提供的各种属性和方法
"""

class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self._age = age
        self.__gender = gender

p1 = Person("张三",18,"男")
print(p1.__dict__)  # 自己的
print(dir(p1))      # 可以访问到的所有的,包括自己的和继承的