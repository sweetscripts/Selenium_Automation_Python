import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#available scopes are:
#function, class, module, package or session
@pytest.fixture(scope="function")
def driver():
    options = Options()
    #arguments are awailable --headless, --disable-gpu, --window-size=1280x720 etc.
    #options.add_argument("--headless")  # Run Chrome in headless mode.
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def url():
    return 'https://www.saucedemo.com/'

@pytest.fixture
def login(driver, url):
    driver.get(url)
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.NAME, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()
    assert driver.title == "Swag Labs"

# @pytest.fixture(scope="class")
# def login_class(driver_class):
#     url = 'https://www.saucedemo.com/'
#     driver_class.get(url)
#     driver_class.find_element(By.ID, 'user-name').send_keys('standard_user')
#     driver_class.find_element(By.NAME, 'password').send_keys('secret_sauce')
#     driver_class.find_element(By.ID, 'login-button').click()
#     assert driver_class.title == "Swag Labs"

# @pytest.fixture(scope="class")
# def driver_class():
#     options = Options()
#     #arguments are awailable --headless, --disable-gpu, --window-size=1280x720 etc.
#     options.add_argument("--headless")
#     driver = webdriver.Chrome(options=options)
#     yield driver
#     driver.quit()
