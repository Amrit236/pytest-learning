import pytest
from playwright.sync_api import Page

BASE_URL = https://opensource-demo.orangehrmlive.com/"
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


def navigate_to_education(page: Page):
    page.click("text=Admin")
    page.click("text=Qualifications")
    page.click("text=Education")
    page.wait_for_selector("text=Education")


def test_add_education(setup):
    page = setup

    # Login
    login(page)

    # Navigate to Education
    navigate_to_education(page)

    # Click Add button
    page.click("button:has-text('Add')")

    # Fill Level field
    page.fill("input[class*='oxd-input']", "Bachelor Degree")

    # Click Save
    page.click("button:has-text('Save')")

    # Verify success message
    page.wait_for_selector("text=Successfully Saved")

    assert page.locator("text=Successfully Saved").is_visible()