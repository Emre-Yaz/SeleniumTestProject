import unittest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
# from selenium.webdriver.chrome.service import Service
import page


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        print("setup")
        self.options = ChromeOptions()
        self.options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(self.options)
        self.driver.get("http://www.python.org")

    '''def setUp(self):              #Can be used also
        self.PATH = "C:/Users/monster/PycharmProjects/TestSeleniumProject/Driver/chromedriver.exe"
        self.s = Service(self.PATH)
        self.driver = webdriver.Chrome(service=self.s)
        self.driver.get("http://www.python.org")'''

    # If the method name starts with "test" it'll automatically run.
    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
