from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# EMAIL
# PASSWORD

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options= chrome_options)

driver.get(url= "https://www.linkedin.com/jobs/collections/easy-apply/?currentJobId=4235373748&discover=recommended&discoveryOrigin=JOBS_HOME_JYMBII")

# time.sleep(5)
#
# x_off = driver.find_element(By.XPATH, value= '/html/body/div[6]/div/div/section/button/icon/svg')
# x_off.click()

time.sleep(3)

# sign_in = driver.find_element(By.XPATH, value= '/html/body/div[6]/div/div/section/div/div/div/div[2]/button')
# sign_in.click()
#
# time.sleep(2)

email_entry = driver.find_element(By.XPATH, value= '/html/body/div/main/div[3]/div[1]/form/div[1]/input')
email_entry.click()
email_entry.send_keys(EMAIL)

time.sleep(2)

password_entry = driver.find_element(By.XPATH, value= '/html/body/div/main/div[3]/div[1]/form/div[2]/input')
password_entry.click()
password_entry.send_keys(PASSWORD)

sign_in_button = driver.find_element(By.XPATH, value= '/html/body/div/main/div[3]/div[1]/form/div[4]/button')
sign_in_button.click()

time.sleep(2)

easy_apply = driver.find_element(By.XPATH, value= '/html/body/div[7]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div/div[6]/div/div/div/button')
easy_apply.click()

time.sleep(1)

next_button = driver.find_element(By.XPATH, value= '/html/body/div[4]/div/div/div[2]/div/div[2]/form/footer/div[2]/button')
next_button.click()

time.sleep(1)

next_next_button = driver.find_element(By.XPATH, value= '/html/body/div[4]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]')
next_next_button.click()

time.sleep(30)
# driver.quit()
