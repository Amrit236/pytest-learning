import pytest
from playwright.sync_api import Page

BASE_URL = "https://opensource-demo.orangehrmlive.com/"
USERNAME = "Admin"
PASSWORD = "admin123"


@pytest.fixture(scope="function")
def setup(page: Page):
    page.goto(BASE_URL)
    yield page


def login(page: Page):
    page.fill("input[name='username']", USERNAME)
    page.fill("input[name='password']", PASSWORD)
    page.click("button[type='submit']")
    page.wait_for_selector("text=Dashboard")


def navigate_to_general_info(page: Page):
    page.click("text=Admin")
    page.click("text=Organization")
    page.click("text=General Information")
    page.wait_for_selector("text=General Information")


def test_edit_general_information(setup):
    page = setup

    # Login
    login(page)

    # Navigate
    navigate_to_general_info(page)

    # Click Edit
    page.click("text=Edit")

    # Update Organization Name
    page.fill("input[class*='oxd-input']", "My Test Company")

    # Click Save
    page.click("text=Save")

    # Verify success message
    page.wait_for_selector("text=Successfully Saved")

    assert page.locator("text=Successfully Saved").is_visible()