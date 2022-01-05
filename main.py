from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

CHROME_DRIVER_PATH = ""
SIMILAR_ACCOUNT = ""
USERNAME = ""
PASSWORD = ""


class InstaFollower():
    def __init__(self, path):
        self.driver = webdriver.Chrome(service=Service(path))

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")

        sleep(3)
        email = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        email.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)

        sleep(3)
        save_information = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/section/div/button')
        save_information.click()
        sleep(3)
        turn_off_notifications = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
        turn_off_notifications.click()

    def find_followers(self):
        sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        sleep(3)
        followers = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        sleep(3)
        modal = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollIntoView(true);", modal)
            sleep(3)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for each_button in all_buttons:
            try:
                each_button.click()
                sleep(2)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
