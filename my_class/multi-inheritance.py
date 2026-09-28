"""

多重继承

"""


# 类1
class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def speak(self):
        print(f"我叫{self.name},{self.age}岁,性别{self.gender}")

# 类2
class Worker:
    def __init__(self,company):
        self.company = company
    def work(self):
        print(f'我在{self.company}做兼职')

# 类3
class Student(Person,Worker):
    def __init__(self,name,age,gender,company,id,grade):
        Person.__init__(self,name,age,gender)
        Worker.__init__(self,company)
        self.id = id
        self.grade = grade
    def my(self):
        print(f'学号{self.id},年级{self.grade}')

p = Student("老王",18,"男","乐乐",24,"二年纪")
p.my()

"""
类的 __mro__ 属性：用于记录属性和方法的查找顺序
通过实例去查找属性或方法是，会先在实例身上找，没有就按照__mro__记录的顺序找
"""
print(Student.__mro__)

