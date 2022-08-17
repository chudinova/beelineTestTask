from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def go_to_site(self, url):
        self.driver.get(url)

    def click_element(self, locator):
        self.find_element(locator).click()

    def is_element_displayed(self, locator):
        return self.find_element(locator).is_displayed()

    def send_keys(self, locator, keys):
        self.find_element(locator).send_keys(keys)

    def is_password_hidden(self, locator):
        return self.find_element(locator).get_attribute(
            "type") == "password"
