from selenium.webdriver.common.by import By

from MyWebsite_POM.Base.base_page import BasePage


class AboutPage(BasePage):
    formBut = (By.XPATH, "//button[@id='jfCard-welcome-start']")
    first_name = (By.ID, "input_1_field_1")
    last_name = (By.ID, "input_1_field_2")
    email = (By.ID, "input_1_field_3")
    phone = (By.ID, "input_1_field_4")
    note = (By.ID, "input_1_field_5")
    submit_button = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def start_form(self):
        frame = self.driver.find_element(By.ID, 'JotFormIFrame-240056577186058')
        self.driver.switch_to.frame(frame)
        self.driver.execute_script("window.scrollTo(0, 6000)")
        self.driver.find_element(*self.formBut).click()

    def fill_form(self):
        self.driver.find_element(*self.first_name).send_keys("emre")
        self.driver.find_element(*self.last_name).send_keys("yaz")
        self.driver.find_element(*self.email).send_keys("ibrahimemreyaz@gmail.com")
        self.driver.find_element(*self.phone).send_keys("5057777777")
        self.driver.find_element(*self.note).send_keys("Hey this message is automated!")

    def submit_form(self):
        self.driver.find_element(*self.submit_button).click()

    def is_form_submitted(self):
        return self.driver.find_element(By.CLASS_NAME, "jfThankYou-header").is_displayed()
