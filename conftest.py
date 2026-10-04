import pytest
from playwright.sync_api import Page, expect


@pytest.fixture
def test_login(page: Page):
    page.goto("https://playwright.dev")
    
    return Page

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot_path = f"screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path)
            print(f"Screenshot saved to {screenshot_path}")