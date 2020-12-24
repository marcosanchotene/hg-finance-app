from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class LoginPage(BasePage):
    PAGE_URL = "financeiro.hostgator.com.br"
    ENTENDI_BUTTON = (By.ID, "cookie-cta")
    ENTRAR_BUTTON = (By.CSS_SELECTOR, "#login .button-yellow")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#login [name='email']")
    PASSWORD_FIELD = (By.ID, "password")
    ESQUECEU_SENHA_LINK = (By.CSS_SELECTOR, ".forgot-link")
    BASE_CONHECIMENTO_LINK = (By.CSS_SELECTOR, ".login-block")
    RECAPTCHA_MESSAGE = (By.CSS_SELECTOR, ".text-danger.help-block")

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)

    def click_entendi_button(self):
        entendi_button = self.wait.until(expected_conditions.visibility_of_element_located(self.ENTENDI_BUTTON))
        entendi_button.click()

    def click_entrar_button(self):
        entrar_button = self.browser.find_element(*self.ENTRAR_BUTTON)
        entrar_button.click()

    def click_esqueceu_senha_link(self):
        esqueceu_senha_link = self.browser.find_element(*self.ESQUECEU_SENHA_LINK)
        esqueceu_senha_link.click()

    def click_base_de_conhecimento_link(self):
        base_de_conhecimento_link = self.browser.find_element(*self.BASE_CONHECIMENTO_LINK)
        base_de_conhecimento_link.click()

    def type_email_address(self, email):
        email_field = self.browser.find_element(*self.EMAIL_FIELD)
        email_field.send_keys(email)

    def type_password(self, password):
        password_field = self.browser.find_element(*self.PASSWORD_FIELD)
        password_field.send_keys(password)

    def is_email_valid(self):
        email_field = self.browser.find_element(*self.EMAIL_FIELD)
        return self.browser.execute_script("return arguments[0].validity.valid;", email_field)

    def is_password_valid(self):
        password_field = self.browser.find_element(*self.PASSWORD_FIELD)
        return self.browser.execute_script("return arguments[0].validity.valid;", password_field)

    def is_captcha_message_displayed(self):
        recaptcha_message = self.wait.until(expected_conditions.visibility_of_element_located(self.RECAPTCHA_MESSAGE))
        return recaptcha_message.is_displayed()

    def verify_page_url(self):
        return super().verify_current_url(self.PAGE_URL)

    def switch_to_new_tab(self):
        self.browser.switch_to.window(self.browser.window_handles[1])
