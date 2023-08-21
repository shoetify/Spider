from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import pandas as pd

website = "https://www.adamchoi.co.uk/overs/detailed"

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=option)
driver.get(website)

# using xpath to find the button
all_matches_button = driver.find_element(by='xpath', value='//label[@analytics-event="All matches"]')
# click on it
all_matches_button.click()

time.sleep(1)

drop_down = Select(driver.find_element(by='id', value='country'))
drop_down.select_by_visible_text('France')


time.sleep(3)

matches = driver.find_elements(by='tag name', value="tr")

date = []
home_team = []
score = []
away_team = []

for match in matches:
    date.append(match.find_element(by='xpath', value='./td[1]').text)
    home_team.append(match.find_element(by='xpath', value='./td[2]').text)
    score.append(match.find_element(by='xpath', value='./td[3]').text)
    away_team.append(match.find_element(by='xpath', value='./td[4]').text)

# quit
driver.quit()

df = pd.DataFrame({
    'date': date,
    'home team': home_team,
    'score': score,
    'away team': away_team,
})
df.to_csv('football_data.csv', index=False)
