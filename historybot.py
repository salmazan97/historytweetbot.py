import time
import random
import selenium
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def getHistory():
    browser = webdriver.Chrome('./chromedriver')
    browser.implicitly_wait(25)
    browser.get(' https://www.britannica.com/on-this-day ' )
    savedTitle = browser.find_element(By.XPATH, '/html/body/main/div/div/div[1]/div[2]/div/div[1]/div/div[2]/div[1]')
    writeTitle = savedTitle.text
    savedHistory = browser.find_element(By.XPATH, '/html/body/main/div/div/div[1]/div[2]/div/div[1]/div/div[2]/div[2]')
    writeHistory = savedHistory.text
    with open('D:\\python\\historybot\\historytext.txt', 'w') as f:
        f.write(writeHistory)
        f.close()
    with open('D:\\python\\historybot\\title.txt', 'w') as t:
        t.write(writeTitle)
        t.close()


getHistory()