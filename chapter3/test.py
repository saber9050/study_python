def hello():
    name = input("请输入名称：")
    age = int(input("请输入年龄"))
    if age < 55:
        print(f"Hello,年轻的{name}")
    else:
        print(f"Hello,老老的{name}")


def my_test():
    list1 = [1,2,3,4]
    list2 = list1
    print(f"list1:{list1}\nlist2{list2}")
    list1.append(5)
    print(f"list1:{list1}\nlist2{list2}")


my_test()
