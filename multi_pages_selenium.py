from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

website = "https://www.audible.com/adblbestsellers?ref=a_search_t1_navTop_pl0cg1c0r0&pf_rd_p=1bb99d4d-8ec8-42a3-bb35-704e849c2bc6&pf_rd_r=24CPR9PH5K098X1TDZGA&pageLoadId=HHUR60HGoNOUJwyH&creativeId=1642b4d1-12f3-4375-98fa-4938afc1cedc&overrideBaseCountry=true&ipRedirectOverride=true&pf_rd_p=3b01d5da-1bf0-4646-924a-440835f79703&pf_rd_r=9JMR7K4JCSP41ADH49CQ&pageLoadId=H7euo4kGStIFXfQX&creativeId=7e5ef24f-29c2-42b4-9ad7-cdff92184a00"

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
# option.add_argument('--headless')
# option.add_argument('window-size=1920x1080')

driver = webdriver.Chrome(options=option)
driver.get(website)
driver.maximize_window()

time.sleep(2)

book_title = []
book_author = []
book_length = []

# pagination

# found out how many page totally
pagination = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//ul[contains(@class, "pagingElements")]'))
)
# pagination = driver.find_element(by='xpath', value='//ul[contains(@class, "pagingElements")]')
pages = pagination.find_elements(by='tag name', value='li')
lastpage = int(pages[-2].text)

current_page = 1

while current_page <= lastpage:
    container = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'adbl-impression-container')))
    # container = driver.find_element(by='class name', value='adbl-impression-container ')
    products = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.XPATH, './/li[contains(@class, "productListItem")]'))
    )
    #products = container.find_elements(by='xpath', value='.//li[contains(@class, "productListItem")]')

    for product in products:
        book_title.append(product.find_element(by='xpath', value=".//h3[contains(@class, 'bc-heading')]").text)
        book_author.append(product.find_element(by='xpath', value=".//li[contains(@class, 'authorLabel')]").text)
        book_length.append(product.find_element(by='xpath', value=".//li[contains(@class, 'runtimeLabel')]").text)

    current_page += 1

    try:
        next_page = driver.find_element(by='xpath', value="//span[contains(@class, 'nextButton')]")
        next_page.click()
    except:
        pass

driver.quit()

df_books = pd.DataFrame({
    'title': book_title,
    'author': book_author,
    'length': book_length,
})

df_books.to_csv('books.csv', index=False)
