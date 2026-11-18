from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain2.mytool import get_weather
from langchain.messages import HumanMessage


key = ""
model = init_chat_model("deepseek-chat",
                        model_provider="deepseek",
                        api_key = key)

my_tools = [get_weather]

agent = create_agent(model,tools=my_tools)

messages = {"messages":[HumanMessage("武汉天气怎么样")]}

response = agent.invoke(messages)
print(response['messages'][-1].content)