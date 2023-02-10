from asyncio import sleep

from dropdown_page import DropdownButton


def test_dropdown_button(browser):
    dropdown_page = DropdownButton(browser)
    dropdown_page.click_dropdown_button()
    dropdown_page.select_option_one()
    # dropdown_page.select_option_two()
    sleep(10)

