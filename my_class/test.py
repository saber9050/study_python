class Dog:
    # 构造方法
    # 注意：后面的类型只是提示，如果类型不一样也不会报错，不会做校验
    def __init__(self,name:str,age:int):
        self.name = name
        self.age = age
    # 自我介绍方法
    def introduce(self):
        print(f"我叫{self.name},年龄{self.age}")

d1 = Dog("大黄",3)
d1.introduce()

# 临时扩展属性，不会影响类本身
d1.like = "草莓"

print(d1.like)



# 类继承
class YellowDog(Dog):
    def __init__(self,  name: str, age: int,like: str):
        super().__init__(name, age)
        self.like = like

    def my_like(self):
        print(f"我喜欢{self.like}")

y = YellowDog("橘子狗","i","石头")
print(y.age)