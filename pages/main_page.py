from random import randint
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPageLocators:
    LOCATOR_ENTER_BUTTON = (By.CSS_SELECTOR, '.MgQFWr.Ynb9Xm.mS4uL4')
    LOCATOR_PERMANENT_PASSWORD_AUTH_CHOOSE_BUTTON = (By.CSS_SELECTOR, 'div.am0fm7>div>ul>li:nth-child(3)>button')
    LOCATOR_PERMANENT_PASSWORD_AUTH_LOGIN_FIELD = (By.CSS_SELECTOR, '[placeholder="Логин"]')
    LOCATOR_PERMANENT_PASSWORD_AUTH_PASSWORD_FIELD = (By.CSS_SELECTOR, '[placeholder="Пароль"]')
    LOCATOR_PERMANENT_PASSWORD_AUTH_SUBMIT_BUTTON = (By.CSS_SELECTOR, '.d3jkWo')


class MainPageAuth(BasePage):

    def enter_auth_menu(self):
        return self.find_element(MainPageLocators.LOCATOR_ENTER_BUTTON).click()

    def auth_method_with_permanent_password_choose(self):
        return self.find_element(MainPageLocators.LOCATOR_PERMANENT_PASSWORD_AUTH_CHOOSE_BUTTON).click()

    def auth_method_with_permanent_password_login_enter(self):
        ctn = randint(9000000000, 9999999999)
        self.find_element(MainPageLocators.LOCATOR_PERMANENT_PASSWORD_AUTH_LOGIN_FIELD).send_keys(ctn)

    def auth_method_with_permanent_password_password_enter(self):
        psw = randint(000000, 999999)
        return self.find_element(MainPageLocators.LOCATOR_PERMANENT_PASSWORD_AUTH_PASSWORD_FIELD).send_keys(psw)

    def auth_method_with_permanent_password_submit_button_click(self):
        return self.find_element(MainPageLocators.LOCATOR_PERMANENT_PASSWORD_AUTH_SUBMIT_BUTTON).click()
