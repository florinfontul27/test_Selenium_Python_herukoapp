from asyncio import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class DropdownButton:

    DROPDOWN_BUTTON = (By.CSS_SELECTOR, "div>#dropdown")
    SELECT_OPTION_ONE = (By.CSS_SELECTOR, "#dropdown > option:nth-child(2)")
    SELECT_OPTION_TWO = (By.CSS_SELECTOR, "#dropdown > option:nth-child(3)")


    def __init__(self, browser):
        self.browser = browser

    def click_dropdown_button(self):
         self.browser.find_element(*self.DROPDOWN_BUTTON).click

    def select_option_one(self):
        self.browser.find_element(*self.SELECT_OPTION_ONE).click

    def select_option_two(self):
        self.browser.find_element(*self.SELECT_OPTION_TWO).click


