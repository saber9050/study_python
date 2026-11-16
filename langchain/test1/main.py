# 模型
from langchain.chat_models import init_chat_model
from openai import api_key
# 导入用户问题、助手提示词、系统提示词
from langchain.messages import HumanMessage,AIMessage,SystemMessage
# SystemMessage（系统消息）：给 AI 定全局规则、身份、约束，是底层指令，一般放在对话最开头。
# HumanMessage（人类消息）：用户说的话，用户提问 / 输入。
# AIMessage（AI 消息）：可充做历史对话记录




# 设置密钥
key = "sk-xxx"

model = init_chat_model("deepseek-chat",
                        model_provider="deepseek",
                        api_key = key)

test1 = [
    # SystemMessage("你是一个专业的数学家"),
    # HumanMessage("25+10是多少"),
    AIMessage("25+10=35"),
    HumanMessage("再加10呢")
]



# response = model.invoke("你是什么？")
# print(response)

response = model.invoke(test1)
print(response)