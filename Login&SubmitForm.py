# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Initialize the WebDriver
chrome_options = webdriver.ChromeOptions()
service = Service(executable_path="C:/Users/monster/PycharmProjects/TestSeleniumProject/Driver/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

# Load my webpage
driver.get("https://emre-yaz.github.io/test.html")

# Enter credentials
username_input = driver.find_element(By.ID, "username")
username_input.send_keys("emre")

password_input = driver.find_element(By.ID, "password")
password_input.send_keys("password")

# Click login
login_button = driver.find_element(By.TAG_NAME, "button")
login_button.click()

# Switch to iframe mode?
driver.implicitly_wait(15)
frame = driver.find_element(By.ID, 'JotFormIFrame-240056577186058')
driver.switch_to.frame(frame)

# Find form button via XPATH and click
formBut = driver.find_element(By.XPATH, "//button[@id='jfCard-welcome-start']")
formBut.click()

# Fill out the form
fn = driver.find_element(By.ID, "input_1_field_1")
fn.send_keys("emre")

ln = driver.find_element(By.ID, "input_1_field_2")
ln.send_keys("yaz")

ema = driver.find_element(By.ID, "input_1_field_3")
ema.send_keys("ibrahimemreyaz@gmail.com")

pn = driver.find_element(By.ID, "input_1_field_4")
pn.send_keys("5057777777")

note = driver.find_element(By.ID, "input_1_field_5")
note.send_keys("Hey!")

# Find submit button via XPATH and click
subBut = driver.find_element(By.XPATH, "//button[@type='submit']")
subBut.click()

