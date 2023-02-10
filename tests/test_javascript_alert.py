from assertpy import assert_that

from pages.alerts_page import AlertsPage

def test_alert_accept(browser):
    alert_page = AlertsPage(browser)
    alert_page.load_page()
    alert_page.open_alert()
    alert_page.accept_alert()
    assert_that(alert_page.get_text_from_result()).is_equal_to("You successfully clicked an alert")

def test_confirm_accept(browser):
    alert_page = AlertsPage(browser)
    alert_page.load_page()
    alert_page.open_confirm()
    alert_page.accept_alert()
    assert_that(alert_page.get_text_from_result()).is_equal_to("You clicked: Ok")

def test_confirm_dismiss(browser):
    alert_page = AlertsPage(browser)
    alert_page.load_page()
    alert_page.open_confirm()
    alert_page.cancel_alert()
    assert_that(alert_page.get_text_from_result()).is_equal_to("You clicked: Cancel")

def test_prompt_accept(browser):
    alert_page = AlertsPage(browser)
    alert_page.load_page()
    alert_page.open_promt()
    alert_page.accept_alert()
    assert_that(alert_page.get_text_from_result()).is_equal_to("You entered:")
    alert_page.open_promt()
    alert_page.insert_text_in_alert("text")
    alert_page.accept_alert()
    assert_that(alert_page.get_text_from_result()).is_equal_to("You entered: text")

def test_confirm_dismiss(browser):
    alert_page = AlertsPage(browser)
    alert_page.load_page()
    alert_page.open_promt()
    alert_page.cancel_alert()
    assert_that(alert_page.get_text_from_result()).is_equal_to("You entered: null")
    alert_page.open_promt()
    alert_page.insert_text_in_alert("text")
    alert_page.cancel_alert()
    assert_that(alert_page.get_text_from_result()).is_equal_to("You entered: null")