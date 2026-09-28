# 高阶函数：函数的 参数 或 返回值 是函数，那就是高阶函数

# 意义：
# 1.代码复用率高，可以把行为“独立出去”，传入不同函数实现不同逻辑
# 2.能让函数更灵活通用
# 3.高阶函数是装饰器、闭包的基础

def info(msg):
    return '[提示]:' + msg

def log(func,msg):
    print(func(msg))

def log2(msg):
    return info(msg)

log(info,"成功啦")
print(log2("666"))