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


def navigate_to_skills(page: Page):
    page.click("text=Admin")
    page.click("text=Qualifications")
    page.click("text=Skills")
    page.wait_for_selector("text=Skills")


def test_add_skill(setup):
    page = setup

    # Login
    login(page)

    # Navigate to Skills
    navigate_to_skills(page)

    # Click Add button
    page.click("button:has-text('Add')")

    # Fill Skill Name
    page.fill("input[class*='oxd-input']", "Python Automation")

    # Fill Description
    page.fill("textarea", "Automation testing using Playwright and Pytest")

    # Click Save
    page.click("button:has-text('Save')")

    # Verify Success Message
    page.wait_for_selector("text=Successfully Saved")

    assert page.locator("text=Successfully Saved").is_visible()