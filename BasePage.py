from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as es
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 10)

    def open(self):
        self.driver.get(self.url)

    def is_visible(self, by_locator) -> WebElement:
        return self.wait.until(es.visibility_of_element_located(by_locator))