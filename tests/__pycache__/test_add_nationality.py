import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://your-app-url.com/admin/nationalities"


def test_add_nationality(driver):
    driver.get(BASE_URL)

    wait = WebDriverWait(driver, 10)

    # Click "Add Nationality" button (adjust locator if needed)
    add_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add')]"))
    )
    add_button.click()

    # Enter nationality name
    name_input = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//input[@name='name']"))
    )
    name_input.send_keys("Test Nationality")

    # Click Save
    save_button = driver.find_element(By.XPATH, "//button[contains(text(),'Save')]")
    save_button.click()

    # Verify success message or list update (adjust as needed)
    success_message = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'success')]"))
    )

    assert success_message.is_displayed()
