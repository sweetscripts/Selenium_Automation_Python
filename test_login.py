from selenium.webdriver.common.by import By
import pytest

# tests the login with a negative test
def test_login_negative(driver, url):
    driver.get(url)
    driver.find_element(By.ID, 'user-name').send_keys('locked_out_user')
    driver.find_element(By.NAME, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()

    assert driver.title == "Swag Labs"
    assert driver.find_element(By.CSS_SELECTOR, 'h3').text == "Epic sadface: Sorry, this user has been locked out."


# tests the login with a positive test
def test_login_positive(driver, url):
    driver.get(url)
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.NAME, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()

    assert driver.title == "Swag Labs", "Failed to login."

