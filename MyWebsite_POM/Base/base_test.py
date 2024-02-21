import unittest
from selenium import webdriver


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = self.get_driver("Chrome")  # Adjust the default driver if needed
        self.driver.get("https://emre-yaz.github.io/test.html")
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

    def get_driver(self, driver_name):
        if driver_name == "Chrome":
            return webdriver.Chrome()
        elif driver_name == "Firefox":
            return webdriver.Firefox()
        elif driver_name == "Edge":
            return webdriver.Edge()
        else:
            raise ValueError(f"Invalid driver name: {driver_name}")

    def tearDown(self):
        self.driver.quit()
