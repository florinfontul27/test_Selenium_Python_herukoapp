from selenium.webdriver.common.by import By

class CheckboxesPage:

    #URL
    URL = "https://the-internet.herokuapp.com/checkboxes"

    def __init__(self, browser):
       self.browser = browser

    def loadPage(self):
        self.browser.get(self.URL)

    def is_checkbox_selected(self, order):
        return self.browser.find_element(By.CSS_SELECTOR, f'#checkboxes input:nth-of-type({order})').is_selected()

    def click_checkbox(self, order):
        return self.browser.find_element(By.CSS_SELECTOR, f'#checkboxes input:nth-of-type({order})').click()