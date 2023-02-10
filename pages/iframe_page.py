from selenium.webdriver.common.by import By
from time import sleep


class IframePage:

    TITLE_PAGE = (By.CSS_SELECTOR, "h3")
    IFRAME = (By.CLASS_NAME, "tox-edit-area__iframe")
    EDIT_SECTION = (By.CLASS_NAME, "mce-content-body")
    TEXT_FROM_EDIT = (By.CSS_SELECTOR, ".mce-content-body > p")
    BOLD = (By.CSS_SELECTOR, "[title = 'Bold']")

    #URL
    URL = "https://the-internet.herokuapp.com/iframe"

    def __init__(self, browser):
       self.browser = browser

    def loadPage(self):
        self.browser.get(self.URL)

    def getTitlePage(self):
        return self.browser.find_element(*self.TITLE_TEXT).text

    def write(self, text):
        iframe = self.browser.find_element(*self.IFRAME)
        self.browser.switch_to.frame(iframe)
        self.browser.find_element(*self.EDIT_SECTION).clear()
        sleep(5)
        self.browser.find_element(*self.EDIT_SECTION).send_keys(text)
        sleep(5)

    def get_text(self):
        iframe = self.browser.find_element(*self.IFRAME)
        self.browser.switch_to.frame(iframe)
        self.browser.find_element(*self.EDIT_SECTION).clear()
        sleep(5)
        return self.browser.find_element(*self.TEXT_FROM_EDIT).text