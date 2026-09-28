"""
类的三种权限
"""

class Person:
    def __init__(self,name,age,gender):
        self.name = name      #公有：当前类中、子类、外部都可访问
        self._age = age        #受保护：当前类中、子类都可访问
        self.__gender = gender  #私有：仅有当前类中可访问
    def speak(self):
        print(f'我叫{self.name},年龄{self._age},性别{self.__gender}')

class Student(Person):
    def hello(self):
        print(self.name,self._age)

s = Student("老王",99,"男")
s.hello()
s.speak()
# 在类外部，也可强制访问【背保护的属性】，但不推荐
# 再类外部，不能访问到【私有属性】，会报错