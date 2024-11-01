import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get('https://owa.mos.ru/owa/auth/logon.aspx?replaceCurrent=1&url=https%3a%2f%2fowa.mos.ru%2fowa%2f')
    yield browser
    browser.quit()