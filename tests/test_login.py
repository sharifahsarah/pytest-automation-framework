from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage

import time

def test_open_browser():

    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service)

    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)

    login_page.login("standard_user", "secret_sauce")

    time.sleep(5)
    assert "inventory" in driver.current_url

    driver.quit()