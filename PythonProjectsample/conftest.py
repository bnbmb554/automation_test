import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    #Comment Added by Vivek
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield page
    browser.close()
    playwright.stop()
