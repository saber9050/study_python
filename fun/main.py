"""
函数
def 函数名（参数列表）:
    函数体
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