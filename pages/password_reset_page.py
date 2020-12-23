from pages.base_page import BasePage


class PasswordResetPage(BasePage):
    PAGE_URL = "passwordreset.php"

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def verify_page_url(self):
        return super().verify_current_url(self.PAGE_URL)
