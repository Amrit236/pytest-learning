import pytest
from playwright.sync_api import expect

BASE_URL = "https://opensource-demo.orangehrmlive.com"

def test_add_system_user(page):

    # Open URL
    page.goto(BASE_URL)

    # Login
    page.fill("input[name='username']", "Admin")
    page.fill("input[name='password']", "admin123")
    page.click("button[type='submit']")

    # Click Admin menu
    page.click("text=Admin")

    # Click Add button
    page.click("button:has-text('Add')")

    # Select User Role
    page.click("div:has-text('Select') >> nth=0")
    page.click("text=Admin")

    # Select Status
    page.click("div:has-text('Select') >> nth=1")
    page.click("text=Enabled")

    # Enter Employee Name (type and select first suggestion)
    page.fill("input[placeholder='Type for hints...']", "Paul")
    page.keyboard.press("ArrowDown")
    page.keyboard.press("Enter")

    # Enter Username
    page.fill("input:near(:text('Username'))", "pytestuser123")

    # Enter Password
    page.fill("input[type='password'] >> nth=0", "Test@1234")
    page.fill("input[type='password'] >> nth=1", "Test@1234")

    # Click Save
    page.click("button:has-text('Save')")

    # Verify user appears in list
    page.fill("input[placeholder='Search']", "pytestuser123")
    page.click("button:has-text('Search')")

    expect(page.locator("text=pytestuser123")).to_be_visible()