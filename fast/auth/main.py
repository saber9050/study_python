# Depends：FastAPI 的依赖注入工具，用来把「另一个函数的结果」自动塞进当前函数的参数里。
from fastapi import FastAPI,Depends

# BaseModel：Pydantic 的模型基类，用来定义数据结构并做校验。
from pydantic import BaseModel

# OAuth2PasswordBearer：FastAPI 内置的 OAuth2「密码流」安全方案，
# 作用是从请求头里读取 Authorization: Bearer <token>。
from fastapi.security import OAuth2PasswordBearer

# Annotated：Python 3.9+ 的类型注解增强，FastAPI 推荐用它来写依赖，写法更清晰。
from typing import Annotated

app = FastAPI()

# 告诉 FastAPI：本项目用 Bearer Token 认证
auth_scheme = OAuth2PasswordBearer(tokenUrl="token")

# 用户模型
class User(BaseModel):
    username : str
    password : str

# 假实现：真实项目里应该在这里校验 JWT / 查数据库
def decode_token(token):
    return User(username="老王",password=token)

# 获取当前用户
async def get_current_user(token:Annotated[str,Depends(auth_scheme)]):
    return decode_token(token)

# 访问 GET /user 时，FastAPI 先执行 get_current_user（它又会先执行 auth_scheme），
# 把结果注入到 current 参数。
#
# 最终返回当前用户对象。
@app.get("/user")
async def read_user(current:Annotated[User,Depends(get_current_user)]):
    return current