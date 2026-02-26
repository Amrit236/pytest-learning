from pages.login import login
from pages.login import login

def test_valid_login(page): 
    login_page = login(page)
    login_page.login("Admin", "admin123")
    assert "dashboard" in page.url

def test_invalid_login(page):
    login_page = login(page)
    login_page.login("Admin", "wrongpassword")
    assert "dashboard" in page.url

def test_empty_login(page):
    login_page = login(page)
    login_page.login("admin", "admin123")
    assert "dashboard" in page.url

def test_empty_username(page):
    login_page = login(page)
    login_page.login("Nepal", "admin123")
    assert "dashboard" in page.url

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
