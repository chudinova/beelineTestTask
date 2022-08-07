from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class IdentityPageLocators:
    LOCATOR_WRONG_LOGIN_OR_PASSWORD_ERROR_MESSAGE = (By.XPATH, '//div[text()="Логин и\\или пароль указаны неверно"]')


class IdentityPageElementsFind(BasePage):

    def wrong_login_or_password_error_message(self):
        return self.find_element(IdentityPageLocators.LOCATOR_WRONG_LOGIN_OR_PASSWORD_ERROR_MESSAGE)