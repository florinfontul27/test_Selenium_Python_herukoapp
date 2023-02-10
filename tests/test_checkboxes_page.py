from assertpy import assert_that

from pages.checkbox_page import CheckboxesPage


def test_checkboxes_page(browser):
    checkboxes_page = CheckboxesPage(browser)
    checkboxes_page.loadPage()
    assert_that(checkboxes_page.is_checkbox_selected("1")).is_false()
    assert_that(checkboxes_page.is_checkbox_selected("2")).is_true()
    checkboxes_page.click_checkbox("1")
    checkboxes_page.click_checkbox("2")
    assert_that(checkboxes_page.is_checkbox_selected("1")).is_true()
    assert_that(checkboxes_page.is_checkbox_selected("2")).is_false()