"""

    多态
    python中有两种多态： 标准多态、鸭子多态

    1.标准多态：有继承关系，有方法重写
    2.鸭子多态：指一种编程风格，不检查对象类型，只关注对象能否做到”某件事情“
"""

class Animal:
    def speak(self):
        print("叫~~~")

# 标准多态
class Dog(Animal):
    def speak(self):
        print("汪汪汪")

# 鸭子多态
class Cat:
    def speak(self):
        print("喵喵喵")

def sond(all):
    all.speak()

a = Animal()
d = Dog()
c = Cat()
sond(a)
sond(d)
sond(c)
