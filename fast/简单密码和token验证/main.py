# ==================== 导入的包 ====================

# typing 是 Python 标准库，Annotated 用来给类型加"附加信息"
# 在 FastAPI 里 Annotated[类型, 附加内容] 是声明依赖的推荐写法
from typing import Annotated

# FastAPI 框架本身的核心类
from fastapi import Depends, FastAPI, HTTPException, status

# Depends   : 依赖注入。把一个函数的返回值自动传给路径函数的参数
# FastAPI   : 应用主体类，创建 app 对象用
# HTTPException: 用来主动抛出 HTTP 错误响应（如 401、400）
# status    : 一堆 HTTP 状态码常量，如 status.HTTP_401_UNAUTHORIZED = 401，避免写魔法数字

# OAuth2 相关的安全工具
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# OAuth2PasswordBearer   : 从请求头 Authorization: Bearer <token> 里把 token 抽出来的工具
# OAuth2PasswordRequestForm: 解析"表单格式"的登录请求（字段固定为 username 和 password）
#                           注意它要求前端用 x-www-form-urlencoded 表单提交，不是 JSON

# pydantic 是 FastAPI 用来做数据校验的库
from pydantic import BaseModel, Field

# BaseModel: 所有"数据模型"的基类，继承它就能自动做类型校验
# Field    : 给字段加额外约束，比如默认值、最小长度等

# ==================== 预设的数据（假装是数据库） ====================

# 这里用字典模拟数据库里存的用户表，真实项目里应该是查数据库
# "hashed_password" 是密码的哈希值（这个 demo 是假的哈希，真实项目要用 bcrypt 等算法）
# "disabled" 表示账号是否被禁用
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",  # 即密码是 "secret"
        "disabled": False,  # 正常账号
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",  # 即密码是 "secret2"
        "disabled": True,  # 被禁用的账号
    },
}

# 创建 FastAPI 应用实例
app = FastAPI()


# ==================== 假的密码哈希函数 ====================

# 真实项目应该用 passlib/bcrypt 对密码做不可逆加密
# 这里只是演示流程，直接在明文前面拼个前缀装装样子
def fake_hash_password(password: str):
    return "fakehashed" + password


# ==================== OAuth2 密码模式配置 ====================

# tokenUrl="token" 只是告诉自动生成的文档（/docs）：获取 token 的接口路径是 /token
# 它不会自动创建 /token 接口，接口还是要自己写（见下面 login 函数）
# oauth2_scheme 是一个"可调用对象"，被 Depends() 使用时：
#   -> 从请求头 Authorization: Bearer xxx 中提取出 token 字符串并返回
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# ==================== 数据模型 ====================

# 对外暴露的用户信息（不含密码）
class User(BaseModel):
    username: str = Field(default="老王", min_length=2)  # 默认值"老王"，最少 2 个字符
    email: str | None = None       # 可选字段，None 表示可以为空（str | None 是 Python 3.10+ 写法）
    full_name: str | None = None   # 同上
    disabled: bool | None = None   # 是否禁用


# 数据库里实际存的用户 = 普通用户信息 + 密码哈希
# 继承 User，所以 UserInDB 拥有 User 的所有字段，额外多一个 hashed_password
class UserInDB(User):
    hashed_password: str


# ==================== 工具函数 ====================

# 根据 username 从"数据库"里查用户，转成 UserInDB 对象
# **user_dict 是字典解包：把字典的键值对变成关键字参数传给构造函数
# 查不到返回 None
def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


# 解码 token（假的！）
# 真实项目里 token 是 JWT，这一步要做"验签 + 从 payload 里解析出用户名"
# 这里简化成：token 就是用户名本身，直接拿用户名去查库
def fake_decode_token(token):
    # This doesn't provide any security at all
    # Check the next version
    user = get_user(fake_users_db, token)
    return user


# ==================== 依赖注入链 ====================

# 依赖 1：获取当前登录用户
# 参数 token: Annotated[str, Depends(oauth2_scheme)] 表示——
#   在调用本函数前，先执行 oauth2_scheme（提取请求头里的 Bearer token），结果作为 token 传入
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    if not user:
        # token 无效（查不到用户）→ 返回 401 未授权
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            # WWW-Authenticate: Bearer 是 OAuth2 规范要求的响应头，告诉客户端"请用 Bearer token 方式认证"
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


# 依赖 2：获取"可用的"当前用户（依赖链：依赖里再嵌套依赖）
# 参数 current_user 的值 = 先执行 get_current_user（它又先执行 oauth2_scheme）的结果
async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    if current_user.disabled:
        # 账号被禁用 → 返回 400
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


# ==================== 接口 1：登录，获取 token ====================

# POST /token：OAuth2 规定的取 token 接口
@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    # Depends() 里空着括号：FastAPI 会自动把请求体解析成 OAuth2PasswordRequestForm
    # （表单里必须有 username 和 password 两个字段）
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        # 用户名不存在（故意不区分"用户名错"和"密码错"，防止撞库）
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    # 把用户提交的明文密码做同样的"哈希"，再和库里存的哈希对比
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    # 登录成功，返回 token
    # 这个 demo 里 token 就是用户名（因为 fake_decode_token 靠它查库）
    # 真实项目这里应该是签发的 JWT
    # token_type: "bearer" 是 OAuth2 规范，告诉客户端请求头要写成 Authorization: Bearer <token>
    return {"access_token": user.username, "token_type": "bearer"}


# ==================== 接口 2：查看自己的信息 ====================

# GET /users/me：受保护的接口，必须带有效 token 才能访问
@app.get("/users/me")
async def read_users_me(
    # 完整依赖链：oauth2_scheme 取 token → get_current_user 查用户 → get_current_active_user 检查禁用
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    # 能走到这里说明 token 有效且账号未禁用
    return current_user

# ==================== 整体流程总结 ====================
# 1. 客户端 POST /token，表单里带 username + password
# 2. 服务端校验通过 → 返回 access_token
# 3. 客户端后续每次请求都带请求头 Authorization: Bearer <token>
# 4. oauth2_scheme 从请求头抽 token → 假解码当成用户名 → 查库
# 5. 查到了返回用户信息，被禁用或查不到就报错
