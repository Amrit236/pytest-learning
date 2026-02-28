import os
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://your-app-url.com/admin/corporate-branding"


def test_update_corporate_branding(driver):
    driver.get(BASE_URL)

    wait = WebDriverWait(driver, 10)

    # ----- Select Primary Color -----
    primary_color = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Primary Color')]/following::div[1]"))
    )
    primary_color.click()

    # Example: Select first color option (adjust locator if color picker appears)
    color_option = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'color')]"))
    )
    color_option.click()

    # ----- Upload Client Logo -----
    logo_path = os.path.abspath("assets/logo.png")
    logo_input = driver.find_element(By.XPATH, "//input[@type='file'][1]")
    logo_input.send_keys(logo_path)

    # ----- Upload Client Banner -----
    banner_path = os.path.abspath("assets/banner.png")
    banner_input = driver.find_element(By.XPATH, "(//input[@type='file'])[2]")
    banner_input.send_keys(banner_path)

    # ----- Click Save -----
    save_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Save')]"))
    )
    save_button.click()

    # ----- Verify Success -----
    success_message = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'success')]"))
    )

    assert success_message.is_displayed()
