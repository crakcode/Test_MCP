import os
from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    print(f"FastMCP app running on port {port}")
    mcp.run(host='0.0.0.0', port=port)
