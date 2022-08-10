from random import randint
from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPageAuth(BasePage):

    ctn = randint(9000000000, 9999999999)
    psw = randint(000000, 999999)

    def enter_auth_menu(self):
        return self.find_element(MainPageLocators.LOCATOR_ENTER_BUTTON).click()

    def login_dialog_modal_find(self):
        return self.find_element(MainPageLocators.LOCATOR_LOGIN_DIALOG_MODAL)

    def auth_method_with_permanent_password_choose(self):
        return self.find_element(MainPageLocators.LOCATOR_PERMANENT_PASSWORD_AUTH_CHOOSE_BUTTON).click()

    def auth_method_with_permanent_password_login_enter(self, ctn):
        self.find_element(MainPageLocators.LOCATOR_PERMANENT_PASSWORD_AUTH_LOGIN_FIELD).send_keys(ctn)

    def auth_method_with_permanent_password_password_enter(self, psw):
        return self.find_element(MainPageLocators.LOCATOR_PERMANENT_PASSWORD_AUTH_PASSWORD_FIELD).send_keys(psw)

    def auth_method_with_permanent_password_submit_button_click(self):
        return self.find_element(MainPageLocators.LOCATOR_PERMANENT_PASSWORD_AUTH_SUBMIT_BUTTON).click()

    def is_password_hidden(self):
        return self.find_element(MainPageLocators.LOCATOR_PERMANENT_PASSWORD_AUTH_PASSWORD_FIELD).get_attribute("type") == "password"
