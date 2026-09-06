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
    def __init__(self,  name: str, age: int,like: str,get:str):
        # 校验参数
        if not isinstance(name, str):
            raise TypeError(f"参数name必须为str类型，实际传入：{type(name).__name__}")
        if not isinstance(age, int):
            raise TypeError(f"参数age必须为int类型，实际传入：{type(age).__name__}")
        if not isinstance(like, str):
            raise TypeError(f"参数like必须为str类型，实际传入：{type(like).__name__}")
        if not isinstance(get, str):
            raise TypeError(f"参数get必须为str类型，实际传入：{type(get).__name__}")

        super().__init__(name, age)
        self.like = like
        # 私有属性
        self.__get = get

    def my_like(self):
        print(f"我喜欢{self.like}")

    def my_get(self):
        print(self.__get)

    # 私有方法
    def __println(self):
        print(666)

    # 调用私有方法
    def call_p(self):
        self.__println()

y = YellowDog("橘子狗","i","石头","90")
print(y.age)
y.call_p()
