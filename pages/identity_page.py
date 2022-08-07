from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class IdentityPageLocators:
    LOCATOR_WRONG_LOGIN_OR_PASSWORD_ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-bind="validationMessage: password"]')


class IdentityPageElementsFind(BasePage):

    def wrong_login_or_password_error_message(self):
        return self.find_element(IdentityPageLocators.LOCATOR_WRONG_LOGIN_OR_PASSWORD_ERROR_MESSAGE)
