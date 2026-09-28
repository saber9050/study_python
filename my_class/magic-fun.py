"""
    魔法方法：
    概念：以 __xxx__ 命名的特殊方法
    特点：无需手动调用，只需要准备好这些方法，python会在特定场景自动调用

常用魔法方法：
    __str__：调用print()或str()时
    __len__：调用len()时
    __lt__：执行 对象1 < 对象2 时候
    __gt__：执行 对象1 > 对象2 时候
    __eq__：执行 对象1 == 对象2 时候
    __getattr__：当访问不存在的属性时
"""

class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self._age = age
        self.__gender = gender

    # 魔法方法 __str__ ，打印时自动调用
    def __str__(self):
        return "瞅啥呢"

    # 调用 len() 触发
    def __len__(self):
        return len(self.name)

    # 调用 p1 < p2 触发
    def __lt__(self, other):
        return len(self.name) < len(other.name)

    # 访问不存在属性触发
    def __getattr__(self, item):
        return f"{item}属性不存在"

p = Person("老王",88,"男")
p1 = Person("王富贵",22,"男")
print(p)
print(len(p))
print(p < p1)
print(p.addr)