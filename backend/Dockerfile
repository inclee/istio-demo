# 使用官方的Python依赖库作为父映像

FROM python:3.7-slim

ARG VERSION=v1
ENV VERSION=${VERSION}

# 将工作目录设置为 /app
WORKDIR /app

# 将当前目录内容复制到容器的 /app内
COPY . /app

# 安装flask
RUN pip install --no-cache-dir flask

# 开放端口80以供此应用程序接入
EXPOSE 80 

# 运行app.py（flask应用） 当容器启动时
CMD ["python", "app.py"]