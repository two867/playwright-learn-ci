# ============================================================
# 基于 Playwright 官方镜像，内置浏览器 + 系统依赖，开箱即用
# ============================================================
FROM mcr.microsoft.com/playwright/python:v1.59.0-noble

# 设置工作目录
WORKDIR /app

# 安装 uv（极速 Python 包管理器）
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# 先复制依赖文件，利用 Docker 层缓存
# 依赖不变时重新构建可以跳过安装步骤
COPY pyproject.toml uv.lock ./

# 使用 uv 同步依赖（安装到系统 Python，不创建虚拟环境）
RUN uv sync --frozen --no-dev --no-install-project

# 复制项目文件
COPY . .

# 再次同步，安装项目本身
RUN uv sync --frozen --no-dev

# 创建 output 目录
RUN mkdir -p /app/output

# 默认执行测试
CMD ["uv", "run", "pytest"]
