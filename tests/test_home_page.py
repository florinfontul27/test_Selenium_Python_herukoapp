from pages.home_page import HomePage

def test_click_dropdown_button(browser):
    home_page = HomePage(browser)
    home_page.load_page()
    home_page.click_dropdown_button()
    

