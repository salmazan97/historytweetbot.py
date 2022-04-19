import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Twitterbot():
    def __init__(self, username, password):
        self.browser = webdriver.Chrome('./chromedriver')
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.implicitly_wait(50)
        self.browser.get('https://twitter.com/i/flow/login')
        usernameInput = self.browser.find_element(By.NAME, 'text')
        usernameInput.send_keys(self.username)
        usernameInput.send_keys(Keys.ENTER)
        passwordInput = self.browser.find_element(By.NAME, 'password')
        passwordInput.send_keys('Test1234!!')
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(5)

    def TestTweet(self):
        with open('./historytext.txt', 'r' ) as f:
            funkyword = f.read()
        with open('./title.txt', 'r') as t:
            funkytitle = t.read()
        self.browser.implicitly_wait(50)
        tweetpath = '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div'
        tweet = self.browser.find_element(By.XPATH, tweetpath)
        tweet.send_keys(funkytitle + ': ' + funkyword)
        tweetbutton = self.browser.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div')
        tweetbutton.click()


if __name__ == '__main__':
    username = 'testpyt79627367'
    password = 'Test1234!!'
    t = Twitterbot(username, password)
    t.signIn()
    count = 0
    while count < 1:
        t.TestTweet()
        count += 1

# testpyt79627367
# Test1234!!