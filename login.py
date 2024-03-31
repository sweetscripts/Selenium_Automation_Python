import pytest
from selenium.webdriver.common.by import By

# Define a fixture for logging in
@pytest.fixture(scope="function")
def login(driver):
    driver.get('https://www.saucedemo.com/')
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.NAME, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()
    assert driver.find_element(By.CLASS_NAME, 'app_logo')  # Verify login success
    # No need to return anything if you're just using the driver instance
    # But you can return user-related info if needed