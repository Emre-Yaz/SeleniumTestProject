# Imports
import time

from MyWebsite_POM.Base.base_test import BaseTest
from MyWebsite_POM.Pages.about_page import AboutPage
from MyWebsite_POM.Pages.login_page import LoginPage


# Creating
class LoginAndSubmitForm(BaseTest):
    driver_name = "Chrome"

    def test_login_and_submit_form(self):
        login = LoginPage(self.driver)
        login.enter_user_name("emre")
        login.enter_password("password")
        about_page = login.click_login_button()
        time.sleep(2)

        about = AboutPage(self.driver)
        about.start_form()
        about.fill_form()
        time.sleep(1)
        about.submit_form()
        time.sleep(2)

        self.assertTrue(about.is_form_submitted())
        time.sleep(2)

        self.tearDown()