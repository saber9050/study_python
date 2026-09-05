import os.path

import my_class.test


# 限制输入只能是字符串
def written(s:str):
    with open("test.txt","a+",encoding="utf-8") as f:
        f.write(s)

written("777")

