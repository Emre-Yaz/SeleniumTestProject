from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
chrome_options = webdriver.ChromeOptions()
service = Service(executable_path="C:/Users/monster/PycharmProjects/TestSeleniumProject/Driver/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

TIMES_TO_CLICK = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999

# Functions
def click_cookie(driver):
    cookie = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "bigCookie")))
    actions = ActionChains(driver)
    actions.click(cookie)
    actions.perform()


def purchase_items(driver, count):
    for i in range(1, -1, -1):
        item = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "productPrice" + str(i))))
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()


def get_cookie_count(driver):
    cookie_count = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "cookies")))
    cookie_count_text = cookie_count.text
    if 'million' in cookie_count_text:
        count = int(float(cookie_count_text.split(" ")[0].replace(',', '')) * 1000000)
    elif 'billion' in cookie_count_text:
        count = int(float(cookie_count_text.split(" ")[0].replace(',', '')) * 1000000000)
    else:
        count = int(cookie_count_text.replace(',', '').split(" ")[0])
    return count

try:
    # Load webpage
    driver.get("https://orteil.dashnet.org/cookieclicker/")

    # Lang Select
    lang_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "langSelect-EN")))
    actions = ActionChains(driver)
    actions.click(lang_select)
    actions.perform()

    for _ in range(TIMES_TO_CLICK):
        click_cookie(driver)
        count = get_cookie_count(driver)
        purchase_items(driver, count)

except Exception as e:
    print("An error occurred:", e)