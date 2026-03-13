

from conftest import logger
import logging

import pytest
from playwright.sync_api import sync_playwright 
from pages.login import login

# @pytest.mark.regression 
# def test_valid_login(page): 
#     login_page = login(page)

#     logger.info("Testing valid login with correct credentials")
#     login_page.login("Admin", "admin123")
#     assert "dashboard" in page.url

@pytest.mark.regression
def test_invalid_login(page):
    login_page = login(page)
    login_page.login("Admin", "wrongpassword")
    # assert "dashboard" in page.url

def test_empty_login(page):
    login_page = login(page)
    login_page.login("admin", "admin123")
    

def test_empty_username(page):
    login_page = login(page)
    login_page.login("Nepal", "admin123")
    

def test_empty_password(page):
    login_page = login(page)
    login_page.login("", "")
    assert "dashboard" in page.url

def test_empty_username_password(page):
    login_page = login(page)
    login_page.login("", "")
    assert "dashboard" in page.url  
def test_valid_login(page):
    login_page = login(page)
    login_page.login("Admin", "admin123")
    assert "dashboard" in page.url
