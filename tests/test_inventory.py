from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.debug import pause
import allure


def test_add_backpack_to_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.login("standard_user", "secret_sauce")

    with allure.step("Add backpack to cart"):
        inventory_page.add_backpack_to_cart()

    with allure.step("Verify cart badge"):
        assert inventory_page.get_cart_badge_count() == "1"


def test_remove_backpack_from_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.login("standard_user", "secret_sauce")

    with allure.step("Add backpack to cart"):
        inventory_page.add_backpack_to_cart()

    with allure.step("Remove backpack to cart"):
        inventory_page.remove_backpack_from_cart()

    with allure.step("Wait cart empty"):
        inventory_page.wait_until_cart_empty()

    with allure.step("Verify cart empty"):
        assert inventory_page.get_cart_badge_count() == "0"


def test_add_multiple_items_to_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.login("standard_user", "secret_sauce")

    with allure.step("Add backpack to cart"):
        inventory_page.add_backpack_to_cart()

    with allure.step("Add fleece jacket to cart"):
        inventory_page.add_fleece_to_cart()

    with allure.step("Verify cart badge count"):
        assert inventory_page.get_cart_badge_count() == "2"
