import pytest
from playwright.sync_api import sync_playwright 
from pages.login import login 

@pytest.fixture

def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")                                                                         
        yield page
        browser.close()
