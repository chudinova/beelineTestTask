from pages.base_page import BasePage
from pages.locators import IdentityPageLocators


class IdentityPageElementsFind(BasePage):

    def wrong_login_or_password_error_message(self):
        return self.find_element(IdentityPageLocators.LOCATOR_WRONG_LOGIN_OR_PASSWORD_ERROR_MESSAGE)
