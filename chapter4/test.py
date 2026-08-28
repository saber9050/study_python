# float
a = 4.9
b = 1.23e-4
print(b+a)

# complex 复数
c = 2 + 3j
d = complex(2,3)
print(c)
print(d)
# 实部
print(d.real)
# 虚部
print(d.imag)

# import keyword
# print(keyword.kwlist)

my_list = ["apple","banana","cherry"]
my_tuple = (1,2,3)
my_dict = {"name":"Alice","age":25}

print(my_list,my_tuple,my_dict)

print(int("123"))
print(str(2.14))

print(2/4)
print(3//4)

# 字符串操作
str1 = "abcdefg"
str2 = "hello,everyone"

print("------------ 字符串操作 ------------------")
print(str1[0])
print(str1[-1])
print(str1[-3])
print(str1[2:7])
print(str1[1:-1:2])

# 列表操作
print("============== 列表操作 ================")
cur_list = [1,23,4,5,6,7]

cur_list.append("lkj;l")
print(cur_list,len(cur_list),cur_list.index(23),cur_list.pop(-1),cur_list)
cur_list.reverse()
print(cur_list)

# 元组操作
print("--------------- 元组操作 --------------------")
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[1])
print(max(my_tuple),min(my_tuple),len(my_tuple))

print(list(my_tuple))