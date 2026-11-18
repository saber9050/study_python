from langchain.tools import tool

# 根据城市查找天气的工具
@tool
def get_weather(query:str) -> str:
    """
        用来查询城市天气的工具
    :param query:城市名，比如武汉
    :return:返回该城市的温度和天气
    """
    if query == "武汉":
        return "温度26度，小雨"
    elif query == "北京":
        return "温度30度，多云"
    elif query == "上海":
        return "温度12度，大雨"
    return "仅支持查询武汉、北京、上海的天气"