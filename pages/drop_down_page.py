from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DropDownPage:
    #locators
    SELECT = (By.ID, 'dropdown')

    #URL
    URL = "https://the-internet.herokuapp.com/dropdown"

    def __init__(self, browser):
       self.browser = browser

    def loadPage(self):
        self.browser.get(self.URL)

    def select_by_text(self, text):
        select = Select(self.browser.find_element(*self.SELECT))

        # select by visible text
        select.select_by_visible_text(text)

    def select_by_value(self, value):
        select = Select(self.browser.find_element(*self.SELECT))
        # select by value
        select.select_by_value(value)

    def is_value_selected(self, value):
         return self.browser.find_element(By.CSS_SELECTOR, f'[value="{value}"][selected="selected"]').is_displayed()