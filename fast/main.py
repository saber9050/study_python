from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message:Hello World"}

# 路径参数  ------------------------------------------------------------------
@app.get("/item/{item}")
def get_item(item):
    return {"item:":item}

## 路径参数 - 锁定类型
@app.get("/item2/{item}")
async  def get2(item:int):
    return {"item:":item}

# 预设值
from enum import Enum
class My(str,Enum):
    one = 1
    two = 2

@app.get("/select/{select}")
async def select(select:My):
    res = ""
    if select == My.one:
        res =  "牛逼"
    if select == My.two:
        res =  "垃圾"
    return {"message":res}

# 请求体   ===========================================================
from pydantic import BaseModel
class Item(BaseModel):
    name:str
    des:str | None = None

@app.post("/item3/")
async def create_item(item:Item):
    return item

