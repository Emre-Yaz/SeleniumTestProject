# Imports
from selenium.webdriver.common.by import By

from MyWebsite_POM.Pages.about_page import AboutPage
from MyWebsite_POM.Base.base_page import BasePage


# Creating the LoginPage class
class LoginPage(BasePage):
    # Locators
    user_name = (By.ID, "username")
    password = (By.ID, "password")
    login_button = (By.TAG_NAME, "button")

    # Constructor
    def __init__(self, driver):
        super().__init__(driver)

    # Actions
    def enter_user_name(self, username):
        self.driver.find_element(*self.user_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()
        return AboutPage(self.driver)