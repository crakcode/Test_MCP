import os
from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    # Smithery에서 HTTP 서버로 동작해야 하므로 port 또는 transport="http" 지정
    mcp.run(port=8000, transport="http")

