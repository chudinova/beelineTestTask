from selenium.webdriver.common.by import By


class MainPageLocators:
    LOCATOR_ENTER_BUTTON = (By.CSS_SELECTOR, 'div.personal div button')
    LOCATOR_LOGIN_DIALOG_MODAL = (By.CSS_SELECTOR, '[data-component="LegacyModal"]')
    LOCATOR_PERMANENT_PASSWORD_AUTH_CHOOSE_BUTTON = (By.CSS_SELECTOR, 'div.initial-form div:nth-child(2) li:nth-child(3)')
    LOCATOR_PERMANENT_PASSWORD_AUTH_LOGIN_FIELD = (By.CSS_SELECTOR, '[placeholder="Логин"]')
    LOCATOR_PERMANENT_PASSWORD_AUTH_PASSWORD_FIELD = (By.CSS_SELECTOR, '[placeholder="Пароль"]')
    LOCATOR_PERMANENT_PASSWORD_AUTH_SUBMIT_BUTTON = (By.CSS_SELECTOR, 'div.initial-form__tab-content button[type="submit"]')
    LOCATOR_PASSWORD_HIDDEN_ELEMENT = (By.XPATH, 'div[style="display: none !important;"]')


class IdentityPageLocators:
    LOCATOR_WRONG_LOGIN_OR_PASSWORD_ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-bind="validationMessage: password"]')
