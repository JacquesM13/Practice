from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class TwitterBot:
    def __init__(self):
        self.PASSWORD = 'RGI76efa!X'
        self.email = 'codebreaker747@outlook.com'
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options= self.chrome_options)
        self.download_result = '100'
        self.upload_result = '100'

    def get_internet_speeds(self):
        self.driver.get(url= "https://www.speedtest.net/")
        sleep(3)
        cookies = self.driver.find_element(By.XPATH, value= '/html/body/div[5]/div[2]/div/div/div[2]/div/div/button[2]')
        cookies.click()
        sleep(2)
        go_button = self.driver.find_element(By.XPATH, value= '/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a/span[4]')
        go_button.click()
        sleep(40)
        self.download_result = self.driver.find_element(By.XPATH, value= '/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.upload_result = self.driver.find_element(By.XPATH, value= '/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(f"Download Speed: {self.download_result}Mbps, Upload speed: {self.upload_result}Mbps")

    def tweet_speeds(self):
        self.driver.get('https://x.com/')
        sleep(4)
        try:
            sign_in = self.driver.find_element(By.LINK_TEXT, value= 'Sign in')
        except:
            sign_in = self.driver.find_element(By.XPATH, value= '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[3]/a/div/span/span')

        sign_in.click()
        sleep(3)
        email_input = self.driver.find_element(By.XPATH, value= '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        email_input.click()
        email_input.send_keys(self.email)
        sleep(2)
        next_button = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')
        next_button.click()
        sleep(2)
        try:
            password_field = self.driver.find_element(By.NAME, value= 'password')
        except:
            username = self.driver.find_element(By.XPATH, value= '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            username.send_keys('xplativ3')
            next = self.driver.find_element(By.XPATH, value= '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span')
            next.click()
            sleep(2)
            password_field = self.driver.find_element(By.NAME, value='password')

        password_field.send_keys(self.PASSWORD)
        login_button = self.driver.find_element(By.XPATH, value= '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button')
        login_button.click()
        sleep(5)
        tweet_field = self.driver.find_element(By.CSS_SELECTOR, value= 'div.DraftEditor-editorContainer')
        tweet_field.send_keys(f"Upload Speed: {self.upload_result}Mbps, Download Speed: {self.download_result}Mbps")
        tweet_button = self.driver.find_element(By.XPATH, value= '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span')
        tweet_button.click()