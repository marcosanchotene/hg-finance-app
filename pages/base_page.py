class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def verify_current_url(self, url):
        return url in self.browser.current_url
