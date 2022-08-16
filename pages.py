from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from random import randint

import locators


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://beeline.ru/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)


class MainPage(BasePage):
    ctn = randint(9000000000, 9999999999)
    psw = randint(000000, 999999)

    def enter_auth_menu(self):
        self.find_element(locators.MainPageLocators.LOCATOR_ENTER_BUTTON).click()

    def login_dialog_modal_find(self):
        self.find_element(locators.MainPageLocators.LOCATOR_LOGIN_DIALOG_MODAL)

    def auth_method_with_permanent_password_choose(self):
        self.find_element(locators.MainPageLocators.LOCATOR_PERMANENT_PASSWORD_AUTH_CHOOSE_BUTTON).click()

    def auth_method_with_permanent_password_login_enter(self, ctn):
        self.find_element(locators.MainPageLocators.LOCATOR_PERMANENT_PASSWORD_AUTH_LOGIN_FIELD).send_keys(ctn)

    def auth_method_with_permanent_password_password_enter(self, psw):
        self.find_element(locators.MainPageLocators.LOCATOR_PERMANENT_PASSWORD_AUTH_PASSWORD_FIELD).send_keys(psw)

    def auth_method_with_permanent_password_submit_button_click(self):
        self.find_element(locators.MainPageLocators.LOCATOR_PERMANENT_PASSWORD_AUTH_SUBMIT_BUTTON).click()

    def is_password_hidden(self):
        return self.find_element(locators.MainPageLocators.LOCATOR_PERMANENT_PASSWORD_AUTH_PASSWORD_FIELD).get_attribute(
            "type") == "password"


class IdentityPage(BasePage):

    def wrong_login_or_password_error_message(self):
        return self.find_element(locators.IdentityPageLocators.LOCATOR_WRONG_LOGIN_OR_PASSWORD_ERROR_MESSAGE)
