class Dog:
    # 构造方法
    def __init__(self,name:str,age:int):
        self.name = name
        self.age = age
    # 自我介绍方法
    def introduce(self):
        print(f"我叫{self.name},年龄{self.age}")

d1 = Dog("大黄",3)
d1.introduce()