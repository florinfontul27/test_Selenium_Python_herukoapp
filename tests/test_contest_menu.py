from pages.context_menu_page import ContextMenuPage

def test_context_menu(browser):
    context_menu_page = ContextMenuPage(browser)
    context_menu_page.load_page()
    context_menu_page.open_menu()
    context_menu_page.accept_alert()