from pathlib import Path
from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        # 1. 指定你的用户数据存放路径
        user_data_dir = Path(r"D:\playwright_user_data")

        # 2. 启动同步持久化上下文
        context = p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            headless=False,  # 调试时设为 False 方便观察
            channel="chrome",  # 可选：指定使用标准的 Chrome 浏览器
            args=["--disable-blink-features=AutomationControlled"],  # 防自动化检测
        )

        # 3. 直接从 context 创建页面
        page = context.new_page()

        # 访问网站并操作
        page.goto("https://github.com")
        breakpoint()
        # 此时你可以手动在浏览器里登录，或者执行其他操作
        # 登录成功后，数据会自动保存到 D:\playwright_user_data 目录下

        # 4. 记得关闭上下文以保存数据
        context.close()


if __name__ == "__main__":
    main()