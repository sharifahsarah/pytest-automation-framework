from selenium.webdriver.common.by import By
import allure


class LoginPage:

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        with allure.step("Enter username"):
            self.driver.find_element(*self.USERNAME).send_keys(username)

        with allure.step("Enter password"):
            self.driver.find_element(*self.PASSWORD).send_keys(password)

        with allure.step("Click Login button"):
            self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_error_message(self):
        with allure.step("Get error message"):
            return self.driver.find_element(*self.ERROR_MESSAGE).text



