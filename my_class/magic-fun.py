"""
    概念：以 __xxx__ 命名的特殊方法
    特点：无需手动调用，只需要准备好这些方法，python会在特定场景自动调用
"""

class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self._age = age
        self.__gender = gender

    # 魔法方法 __str__ ，打印时自动调用
    def __str__(self):
        return "瞅啥呢"

p = Person("老王",88,"男")
print(p)