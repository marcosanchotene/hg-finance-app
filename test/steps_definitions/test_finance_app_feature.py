from pytest_bdd import given, when, then, parsers, scenarios
from pages.login_page import LoginPage
from pages.password_reset_page import PasswordResetPage
from pages.support_page import SupportPage
from resources.user import User

HOSTGATOR_FINANCE_URL = "https://financeiro.hostgator.com.br/"
INVALID_EMAILS = {"blank": "",
                  "without the @ symbol": "test",
                  "blank after the @ symbol": "test@"}
PASSWORDS = {"blank": "",
             "invalid": "123"}

scenarios('../features/finance_app.feature')


@given('I am a registered user', target_fixture='user')
def get_registered_user():
    return User(email="valid@email.com", password="valid_password")


@given('I go to the login page', target_fixture="login_page")
def go_to_login_page(browser):
    browser.get(HOSTGATOR_FINANCE_URL)
    login_page = LoginPage(browser)
    return login_page


@when('I click on the Entendi button')
def click_entendi_button(login_page):
    login_page.click_entendi_button()


@when('I click on the Entrar button')
def click_entrar_button(login_page):
    login_page.click_entrar_button()


@when('I click on the Esqueceu sua senha? link')
def click_esqueceu_senha_link(login_page):
    login_page.click_esqueceu_senha_link()


@when('I click on the base de conhecimento link')
def click_base_de_conhecimento_link(login_page):
    login_page.click_base_de_conhecimento_link()


@when(parsers.parse('I type an email address "{email}"'))
@when(parsers.parse('I type a "{email}" email address'))
def type_email_address(login_page, user, email):
    email = user.email if email == "valid" else INVALID_EMAILS[email]
    login_page.type_email_address(email)


@when(parsers.parse('I type a "{state}" password'))
@when(parsers.parse('I type an "{state}" password'))
def type_password(login_page, user, state):
    password = user.password if state == "valid" else PASSWORDS[state]
    login_page.type_password(password)


@then('the email should be considered invalid')
def email_field_is_invalid(login_page):
    assert not login_page.is_email_valid()


@then('the password should be considered invalid')
def password_field_is_invalid(login_page):
    assert not login_page.is_password_valid()


@then('the recaptcha message should be displayed')
def recaptcha_message_is_displayed(login_page):
    assert login_page.is_captcha_message_displayed()


@then('the password reset page should be loaded')
def password_reset_page_is_loaded(browser):
    password_reset_page = PasswordResetPage(browser)
    assert password_reset_page.verify_page_url()


@then('the support page should be loaded on a new tab')
def page_is_loaded_on_new_tab(browser, login_page):
    login_page.switch_to_new_tab()
    support_page = SupportPage(browser)
    assert support_page.verify_page_url()
