from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USERNAME = ''
PASSWORD = ''

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options = chrome_options)

# driver.get('https://www.instagram.com/')
driver.get('https://www.instagram.com/newyorkcity.explore/')

wait = WebDriverWait(driver, 10)

sleep(3)

allow_cookies_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Allow all cookies']")))
allow_cookies_button.click()

# allow_cookies = driver.find_element(By.XPATH, "//button[text()='Allow all cookies']")
# allow_cookies.click()

sleep(3)
try:
    close_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH,
            "//svg[@title='Close' or @aria-label='Close']/ancestor::div[@role='button']"))
    )
    close_btn.click()

except Exception as e:
    pass

# log_in_button = driver.find_element(By.XPATH, "//div[@role='button' and text()='Log in']")
# log_in_button.click()
#
sleep(2)

try:
    username_field = driver.find_element(By.NAME, value= 'username')
    username_field.send_keys(USERNAME)

    password_field = driver.find_element(By.NAME, value= 'password')
    password_field.send_keys(PASSWORD)

    log_in = driver.find_element(By.CSS_SELECTOR, value= '[type="submit"]')
    log_in.click()
except Exception as e:
    log_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='button' and text()='Log In']")))
    log_in_button.click()

    sleep(2)

    username_field = driver.find_element(By.NAME, value= 'username')
    username_field.send_keys(USERNAME)

    password_field = driver.find_element(By.NAME, value= 'password')
    password_field.send_keys(PASSWORD)
    sleep(10)

sleep(2)

not_now_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='button' and normalize-space()='Not now']")))
not_now_btn.click()

sleep(2)

# Wait for and select the followers link
followers_link = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//a[contains(@href, '/followers/') and contains(., 'followers')]")
    )
)

# Example: Click the link (optional)
followers_link.click()

sleep(2)

try:
    follow_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//div[text()='Follow']]")))
    follow_button.click()
    print("✅ Follow button clicked.")
except Exception as e:
    print("❌ Failed to click Follow button:", e)
