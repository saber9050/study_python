from abc import ABC,abstractmethod
"""

抽象类：作为规范，让子类去继承然后实现里面的方法（必须实现），相当于go的接口
实现：继承 ABC 类，就是抽象类

"""

# 一个抽象类
class Test(ABC):
    @abstractmethod
    def run(self):
        pass