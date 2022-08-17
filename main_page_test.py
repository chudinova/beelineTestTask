from pages import BasePage
from locators import MainPageLocators
from locators import IdentityPageLocators
from random import randint


def test_auth_with_permanent_password_and_random_credentials_fail(browser):
    beeline_page = BasePage(browser)
    beeline_page.go_to_site("https://beeline.ru/")
    beeline_page.click_element(MainPageLocators.LOCATOR_ENTER_BUTTON)

    assert beeline_page.is_element_displayed(MainPageLocators.LOCATOR_LOGIN_DIALOG_MODAL), \
        "Login dialog modal window is not displayed"

    beeline_page.click_element(MainPageLocators.LOCATOR_PERMANENT_PASSWORD_AUTH_CHOOSE_BUTTON)
    beeline_page.send_keys(MainPageLocators.LOCATOR_PERMANENT_PASSWORD_AUTH_LOGIN_FIELD, randint(9000000000, 9999999999))
    beeline_page.send_keys(MainPageLocators.LOCATOR_PERMANENT_PASSWORD_AUTH_PASSWORD_FIELD, randint(000000, 999999))

    assert beeline_page.is_password_hidden(MainPageLocators.LOCATOR_PERMANENT_PASSWORD_AUTH_PASSWORD_FIELD), "Password is not hidden"

    beeline_page.click_element(MainPageLocators.LOCATOR_PERMANENT_PASSWORD_AUTH_SUBMIT_BUTTON)

    assert beeline_page.is_element_displayed(IdentityPageLocators.LOCATOR_WRONG_LOGIN_OR_PASSWORD_ERROR_MESSAGE), "Login or password error is not displayed"
