from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage
from langchain_mcp_adapters.client import MultiServerMCPClient
import sys,asyncio

key = ""
model = init_chat_model("deepseek-chat",
                        model_provider="deepseek",
                        api_key = key)

async def main():
    client = MultiServerMCPClient(
        {
            "math":{
                "transport":"stdio",
                "command":sys.executable,#用当前 venv 解释器
                # 文件绝对路径,注意得是列表
                "args":[r"F:\Python_0\project\study\langchain2\calculation.py"]
            }
        }
    )
    my_tools = await client.get_tools()

    agent =  create_agent(model,tools=my_tools)

    messages = {"messages":[HumanMessage("10加6是多少")]}

    response = await agent.ainvoke(messages)

    # 检查mcp输出
    for msg in response["messages"]:
        print(f"[{type(msg).__name__}] {msg.content}")
        if getattr(msg, "tool_calls", None):
            print("  发起调用:", msg.tool_calls)


    print(response['messages'][-1].content)

if __name__ := "__main__":
    asyncio.run(main())