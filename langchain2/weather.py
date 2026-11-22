from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(location:str)->str:
    """获取当地天气"""
    return "今天晴空万里"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")