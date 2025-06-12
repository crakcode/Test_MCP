# Dockerfile

# Python 3.9 Slim Buster 이미지를 베이스로 사용합니다.
FROM python:3.9-slim-buster

# 작업 디렉토리를 /app으로 설정합니다.
WORKDIR /app

# requirements.txt 파일을 컨테이너로 복사하고 의존성을 설치합니다.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드를 컨테이너로 복사합니다.
COPY . .

# 컨테이너가 시작될 때 실행될 명령어를 정의합니다.
# gunicorn을 사용하여 server.py 파일 내의 mcp 인스턴스를 실행합니다.
# 0.0.0.0:${PORT:-8080}은 모든 IP에서 리스닝하며, Smithery가 주입하는 PORT 환경 변수를 사용하고
# PORT가 없을 경우 기본값 8080을 사용합니다.
CMD ["gunicorn", "--bind", "0.0.0.0:${PORT:-8080}", "server:mcp"]