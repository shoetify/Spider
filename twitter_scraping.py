from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

website = "https://twitter.com/search?q=python&src=typed_query"

website1 = "https://www.bilibili.com/"

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=option)
driver.get(website1)
driver.maximize_window()

# Scroll down to bottom
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    else:
        last_height = new_height



# def get_tweet(element):
#     """This function scrapes data of tweets. It returns a list with 2 elements; username and text"""
#     try:
#         user = element.find_element_by_xpath(".//span[contains(text(), '@')]").text  # there are more than 1 but we pick the first
#         text = element.find_element_by_xpath(".//div[@lang]").text
#         tweets_data = [user, text]
#     except:
#         tweets_data = ['user', 'text']
#     return tweets_data
#
#
# tweets = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, "//article[@role='article']")))
#
# user_data = []
# text_data = []
# for tweet in tweets:
#     tweet_list = get_tweet(tweet)  # calling the function get_tweet to scrape data of the tweets list
#     user_data.append(tweet_list[0])  # appending the first element of tweet_list (user)
#     text_data.append(" ".join(tweet_list[1].split()))  # appending the second element of tweet_list (text)
#
# driver.quit()
# df_tweets = pd.DataFrame({
#     'user': user_data,
#     'text': text_data,
# })
# df_tweets.to_csv('tweets.csv', index=False)