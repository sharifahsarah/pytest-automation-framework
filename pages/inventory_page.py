from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:

    ADD_BACKPACK_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_FLEECE_BUTTON = (By.ID, "add-to-cart-sauce-labs-fleece-jacket")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    REMOVE_BACKPACK_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        self.driver = driver

    def add_backpack_to_cart(self):
        self.driver.find_element(*self.ADD_BACKPACK_BUTTON).click()

    def add_fleece_to_cart(self):
        self.driver.find_element(*self.ADD_FLEECE_BUTTON).click()

    def remove_backpack_from_cart(self):
        self.driver.find_element(*self.REMOVE_BACKPACK_BUTTON).click()

    def get_cart_badge_count(self):
        badge = self.driver.find_elements(*self.SHOPPING_CART_BADGE)

        if badge:
            return badge[0].text

        return "0"

    def wait_until_cart_empty(self):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(self.SHOPPING_CART_BADGE)
        )

    def click_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                self.CART_ICON
            )
        ).click()

    def logout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                self.MENU_BUTTON
            )
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                self.LOGOUT_LINK
            )
        ).click()