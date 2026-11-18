# 模型
from langchain.chat_models import init_chat_model
from langchain_core.messages import ToolMessage
# 导入用户问题、助手提示词、系统提示词
from langchain.messages import HumanMessage

# SystemMessage（系统消息）：给 AI 定全局规则、身份、约束，是底层指令，一般放在对话最开头。
# HumanMessage（人类消息）：用户说的话，用户提问 / 输入。
# AIMessage（AI 消息）：可充做历史对话记录




# 设置密钥
key = ""

model = init_chat_model("deepseek-chat",
                        model_provider="deepseek",
                        api_key = key)

# test1 = [
#     # SystemMessage("你是一个专业的数学家"),
#     # HumanMessage("25+10是多少"),
#     AIMessage("25+10=35"),
#     HumanMessage("再加10呢")
# ]
#
#
#
# # response = model.invoke("你是什么？")
# # print(response)
#
# response = model.invoke(test1)
# print(response)

from langchain2.mytool import get_weather

# 工具调用
with_tool = model.bind_tools([get_weather])

messages = [HumanMessage("查询一下上海的天气，告诉我")]
response = with_tool.invoke(messages) # 第一轮，ai调用工具
messages.append(response) # 将ai回复注入

# 查看工具调用 （langchain不会帮你执行，要自己执行工具）
for tool_call in response.tool_calls:
    print(f"工具：{tool_call['name']}")
    print(f"参数：{tool_call['args']}")
    # 执行
    if tool_call['name'] == "get_weather":
        result = get_weather.invoke(tool_call['args'])
        # 注入消息
        messages.append(
            ToolMessage(content=result,tool_call_id=tool_call["id"])
        )

print(model.invoke(messages).content)