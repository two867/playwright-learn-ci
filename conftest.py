import pytest
from playwright.sync_api import BrowserContext, Page


@pytest.fixture
def page(context: BrowserContext) -> Page:
    page = context.new_page()
    page.screencast.show_actions(position="top-right")
    return page

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, pytestconfig, playwright):
    args = {
        **browser_context_args,
        "record_video_size": {
            "width": 1920,
            "height": 1080,
        },  # 合并参数时, 自定义参数（优先级最高）
    }

    if not pytestconfig.getoption("--headed"):  # 有头模式：自适应窗口
        args["viewport"] = {"width": 1920, "height": 1080}

    return args