import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://your-app-url.com/admin/configuration"


def test_update_email_configuration(driver):
    driver.get(BASE_URL)

    wait = WebDriverWait(driver, 10)

    # ---- Update Mail Sent As ----
    mail_input = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//input[contains(@type,'text')]"))
    )
    mail_input.clear()
    mail_input.send_keys("qa_test@mail.com")

    # ---- Select Sending Method: Sendmail ----
    sendmail_radio = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Sendmail')]"))
    )
    sendmail_radio.click()

    # ---- Enable Send Test Mail toggle ----
    toggle = driver.find_element(By.XPATH, "//input[@type='checkbox']")
    driver.execute_script("arguments[0].click();", toggle)

    # ---- Click Save ----
    save_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Save')]"))
    )
    save_button.click()

    # ---- Verify Success Message ----
    success_message = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'success')]"))
    )

    assert success_message.is_displayed()
