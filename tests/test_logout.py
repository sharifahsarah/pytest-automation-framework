from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import allure


def test_logout(driver):

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    with allure.step("Logout from application"):
        inventory_page.logout()

    with allure.step("Verify user redirected to login page"):
        assert driver.current_url == "https://www.saucedemo.com/"
