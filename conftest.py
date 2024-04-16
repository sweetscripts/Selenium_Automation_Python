import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


from BasePage import BasePage
from urls import base_url


#available scopes are:
#function, class, module, package or session
@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    #arguments are awailable --headless, --disable-gpu, --window-size=1280x720 etc.
    #options.add_argument("--headless")  # Run Chrome in headless mode.
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def login_page(driver):
    page = BasePage(driver, base_url)
    return page

