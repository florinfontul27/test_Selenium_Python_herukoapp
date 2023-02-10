from assertpy import assert_that

from pages.iframe_page import IframePage
from time import sleep



def test_iframe_page(browser):
    iframe_page = IframePage(browser)
    iframe_page.loadPage()
    iframe_page.write("anaaa")
    assert_that(iframe_page.get_text()).is_equal_to("anaaa")