from pages.identity_page import IdentityPageElementsFind
from pages.main_page import MainPageAuth


def test_auth_with_permanent_password_and_random_credentials_fail(browser):
    beeline_main_page = MainPageAuth(browser)
    beeline_identity_page = IdentityPageElementsFind(browser)
    beeline_main_page.go_to_site()
    beeline_main_page.enter_auth_menu()
    beeline_main_page.auth_method_with_permanent_password_choose()
    beeline_main_page.auth_method_with_permanent_password_login_enter()
    beeline_main_page.auth_method_with_permanent_password_password_enter()
    beeline_main_page.auth_method_with_permanent_password_submit_button_click()

    assert beeline_identity_page.wrong_login_or_password_error_message().is_displayed()
