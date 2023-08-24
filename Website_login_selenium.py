import pandas as pd
from selenium import webdriver
import setting
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

website = "https://twitter.com/"

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=option)
driver.get(website)

driver.maximize_window()

sign_in_button = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//a[@href='/login']")))

sign_in_button.click()

username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@autocomplete="username"]')))
next_step_button = driver.find_element(by='xpath',
                                       value='//div[@class="css-1dbjc4n r-ywje51 r-nllxps r-jxj0sb r-16wqof r-1dye5f7"]//div[@class="css-901oao r-1awozwy r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0"]')

username.send_keys(setting.USERNAME)
next_step_button.click()

password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@autocomplete="current-password"]')))
login_button = driver.find_element(by='xpath', value='//div[@tabindex="-1"]')

password.send_keys(setting.PASSWORD)
login_button.click()
