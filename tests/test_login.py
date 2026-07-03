
from pages.login_page import LoginPage

import time


def test_successful_login(driver):
    login_page = LoginPage(driver)

    login_page.login("standard_user", "secret_sauce")

    time.sleep(5)
    assert "inventory" in driver.current_url


def test_failed_login(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_use", "secret_sauce")

    error_text = login_page.get_error_message()

    assert "Epic sadface: Username and password do not match any user in this service" in error_text
