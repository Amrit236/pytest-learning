import pytest
from playwright.sync_api import sync_playwright 
from pages.login import login 
import logging
import pytest



@pytest.fixture

def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")                                                                         
        yield page
        browser.close()
      
        @pytest.fixture
        def login(page):
            login = login(page) 
            login.login("Admin", "admin123")
            return login

logging.basicConfig(filename='test.log',
                     level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


@pytest.hookimpl(tryfirst=True,hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield 
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
            page = item.funcargs.get("page")
            screenshot_path = f"screenshot/{item.name}.png"
            page.screenshot(path=screenshot_path)
            logger.info(f"Screenshot taken for failed test: {item.name}")



# def test_valid_login(page, username, password):  
#     login = login(page)
#     login.info(f"Testing valid login with correct credentials")      
#     login.login(username, password)
#     assert "dashboard" in page.url