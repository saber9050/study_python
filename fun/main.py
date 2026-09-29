"""
函数
def 函数名（参数列表）:
    函数体

函数也是对象，也可以动态加属性
"""


def hello():
    print("hello world")

def max(a,b:int):
    if a > b:
        return a
    else:
        return b

hello()
print(max(1,2))

# 匿名函数
x = lambda a: a+10

print(x(8))

print("====")

# 不定长参数
def hello(*args):
    for i in args:
        print(i)

hello(1,2,3)

# 函数作为参数
def call(f):
    f(45)
    print(f'已经调用{f}')

call(hello)

# 多返回值
def calculate(x,y):
    res1 = x + y
    res2 = x - y
    return res1,res2
print(calculate(1,2))

x = lambda a,b:a-b
print(x(1,2))