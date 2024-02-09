from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

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

driver.get("https://emre-yaz.github.io/")
driver.maximize_window()

# Capture the screenshot as binary data
screenshot_binary = driver.get_screenshot_as_png()

# Specify the path and filename for the screenshot
screenshot_path = "screenshots/screenshot.png"

# Save the binary data to a file
with open(screenshot_path, "wb") as file:
    file.write(screenshot_binary)

# Verify the screenshot is saved
if os.path.isfile(screenshot_path):
    print("Screenshot saved successfully at:", os.path.abspath(screenshot_path))
else:
    print("Failed to save the screenshot.")

# Close the WebDriver
driver.close()