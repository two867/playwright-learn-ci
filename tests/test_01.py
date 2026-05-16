import pytest
import allure
from playwright.sync_api import Page, expect


@allure.title("自动化-悬浮")
def test_hover_01(page: Page):
    page.goto("http://www.xn--6frwj470ei1s2kl.com/demo/hover")
    page.get_by_role("button").hover()
    expect(page.locator("#popup")).to_have_text("你已经成功悬浮")


@allure.title("访问百度")
def test_baidu_01(page: Page):
    page.goto("https://www.baidu.com")
    expect(page).to_have_title("百度一下，你就知道")



