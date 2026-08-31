# 集合操作
s1 = {"name","age","height","weight"}
s2 = {"name",1,2,3,"sum"}
print(type(s1))
print(s1 | s2)
print(s1 - s2)
print(s1 & s2)
print(s1 ^ s2)
s1.add(77)
print(s1)