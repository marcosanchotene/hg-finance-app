import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    browser = webdriver.Chrome(options=chrome_options)
    browser.maximize_window()
    yield browser
    browser.quit()
