"""

1. 打包接收参数
    *args   : 打包所有位置参数（形成一个元组）
    **kwargs：打包所有关键字参数（形成一个字典）

2. 解包传递参数 : 人话：固定参数
    *变量名字  ：将元组拆解成一个个独立的位置参数
    **变量名  ：将字典拆解成一个个key=value形式的关键字参数

"""

# 参数打包
def show(*args,**kwargs):
    print(args)
    print(kwargs)

# 参数拆解
def get(a,b,c,name,age):
    print(a,b,c)
    print(name,age)


show(1,2,3,name="牢大",age=18)
get(1,2,3,'牢大',21)