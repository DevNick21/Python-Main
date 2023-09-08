from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time
from dotenv import load_dotenv

load_dotenv()

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")
SPEED_TEST_WEBSITE = "https://www.speedtest.net/"
TWITTER = "https://www.twitter.com/"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.down = 0
        self.up = 0
        self.edge_options = webdriver.ChromeOptions()
        self.edge_options.add_experimental_option("detach", True)

    def get_internet_speed(self):
        driver = webdriver.Chrome(options=self.edge_options)
        driver.get(SPEED_TEST_WEBSITE)
        driver.maximize_window()
        time.sleep(10)
        close_window = driver.find_element(
            By.XPATH, value='//*[@id="onetrust-close-btn-container"]/button')
        close_window.click()
        go = driver.find_element(
            By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go.click()
        time.sleep(70)
        down = driver.find_element(
            By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        up = driver.find_element(
            By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = float(down)
        self.up = float(up)
        driver.quit()

    def tweet_at_provider(self):
        driver = webdriver.Chrome(options=self.edge_options)
        time.sleep(10)
        driver.get(TWITTER)
        driver.maximize_window()
        time.sleep(15)
        sign_in_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div/span/span'
        sign_in = driver.find_element(By.XPATH, value=sign_in_xpath)
        sign_in.click()
        time.sleep(20)
        email_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'
        email = driver.find_element(By.XPATH, value=email_xpath)
        email.send_keys(TWITTER_EMAIL)
        next_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div'
        next_button = driver.find_element(By.XPATH, value=next_xpath)
        next_button.click()
        time.sleep(15)
        password_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
        password = driver.find_element(By.XPATH, value=password_xpath)
        password.send_keys(TWITTER_PASSWORD)
        login_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div'
        login = driver.find_element(By.XPATH, value=login_xpath)
        login.click()
        #! REQUIRES VERIFICATION FOR MY PERSONAL ACCOUNT
        time.sleep(10)
        veri_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div'
        veri_button = driver.find_element(By.XPATH, value=veri_xpath)
        veri_button.click()
        time.sleep(25)
        tweet_xpath = '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div'
        tweet = driver.find_element(By.XPATH, value=tweet_xpath)
        tweet.click()
        time.sleep(10)
        twitting_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div'
        twitting = driver.find_element(By.XPATH, value=twitting_xpath)
        twitting.send_keys(
            f"Hey Internet Provider, why is my internet speed {self.down} down and {self.up} up when i pay for {PROMISED_DOWN}/{PROMISED_UP}?")
        send_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]/div'
        send = driver.find_element(By.XPATH, value=send_xpath)
        send.click()
        time.sleep(5)
        driver.quit()

# !network problem, RUN WHEN NETWORK IS GOOD


speed = InternetSpeedTwitterBot()
speed.get_internet_speed()
speed.tweet_at_provider()
