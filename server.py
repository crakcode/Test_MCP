# server.py
from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    # Smithery는 PORT 환경 변수를 통해 포트를 지정합니다.
    # Gunicorn이 이 PORT 환경 변수를 읽도록 설정할 것입니다.
    # 로컬 테스트를 위해선 mcp.run()에 host와 port를 명시해주는 것이 좋습니다.
    port = int(os.getenv("PORT", 8080)) # PORT 환경 변수 사용
    print(f"FastMCP app running on port {port}")
    mcp.run(host='0.0.0.0', port=port)
