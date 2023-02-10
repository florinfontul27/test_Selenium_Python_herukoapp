from assertpy import assert_that
from pages.drop_down_page import DropDownPage


def test_drop_down(browser):
    drop_down = DropDownPage(browser)
    drop_down.loadPage()
    drop_down.select_by_text("Option 1")
    assert_that(drop_down.is_value_selected("1")).is_true()
    drop_down.select_by_value("2")
    assert_that(drop_down.is_value_selected("2")).is_true()

