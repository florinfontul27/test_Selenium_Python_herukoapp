from asyncio import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class HomePage:
    DROPDOWN_BUTTON = (By.CSS_SELECTOR, "a[href='/dropdown']")
    URL = "https://the-internet.herokuapp.com/"

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def click_dropdown_button(self):
        self.browser.find_element(*self.DROPDOWN_BUTTON).click

