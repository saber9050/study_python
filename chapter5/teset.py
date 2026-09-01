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
s2 = s1.copy()
print(s2)

# 字典操作
d1 = {}
d2 = dict()
print(type(d1),type(d2))
d1["ksl"] = "kjoi"
d1[1]= 99
d1[2]= 888
print(d1.keys(),d1.values())
d1.pop("ksl")
print(d1)
del d1[1]
print(d1)