from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromedriver_path = "C:/Users/monster/PycharmProjects/TestSeleniumProject/Driver/chromedriver.exe"

ser_obj = Service(chromedriver_path)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--enable-features=AllowSyncXHRInPageDismissal")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_experimental_option("prefs", {
    "safebrowsing.enabled": True
})

driver = webdriver.Chrome(service=ser_obj, options=chrome_options)

driver.get("https://bstackdemo.com/")
driver.maximize_window()

try:
    shelfc = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "shelf-container"))
    )

    titles = shelfc.find_elements(by=By.CLASS_NAME,value="shelf-item__title")

    for title in titles:
        print(title.text)

finally:
    driver.quit()
