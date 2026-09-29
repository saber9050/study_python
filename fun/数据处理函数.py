# map函数：对一组数据中的每个元素，统一执行操作，并返回新数据
# 语法：map(操作函数,可迭代对象)，返回的是迭代器对象，要自己遍历或手动转换类型

nums = [1,2,3,4,5]
def double(x):
    return 2 * x

res = map(double,nums)
print(res)
print(list(res))

strs = ["python","go","java"]
res2 = sorted(strs,key=len,reverse=False)
print(res2)