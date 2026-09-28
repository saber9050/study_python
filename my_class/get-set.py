class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self._age = age
        self.__gender = gender

    # 注册age得 get、set方法,访问时自动调用
    @property
    def age(self):
        return self._age

    # set方法，修改时自动调用
    @age.setter
    def age(self,value):
        self._age = value

p = Person("大黄",2,"雄")
print(p.age)
p.age = 99
print(p.age)