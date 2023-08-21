from selenium import webdriver
import pandas as pd
import time

website = "https://www.audible.com/search?overrideBaseCountry=true&ipRedirectOverride=true&pf_rd_p=3b01d5da-1bf0-4646-924a-440835f79703&pf_rd_r=08QZHQ3C0HSZDCAJ0ETS&pageLoadId=6fBtZKl7wYee6mJr&creativeId=7e5ef24f-29c2-42b4-9ad7-cdff92184a00"

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=option)
driver.get(website)
driver.maximize_window()

time.sleep(2)

container = driver.find_element(by='class name', value='adbl-impression-container ')
products = container.find_elements(by='xpath', value='.//li[contains(@class, "productListItem")]')

book_title = []
book_author = []
book_length = []

for product in products:
    book_title.append(product.find_element(by='xpath', value=".//h3[contains(@class, 'bc-heading')]").text)
    book_author.append(product.find_element(by='xpath', value=".//li[contains(@class, 'authorLabel')]").text)
    book_length.append(product.find_element(by='xpath', value=".//li[contains(@class, 'runtimeLabel')]").text)

driver.quit()

df_books = pd.DataFrame({
    'title': book_title,
    'author': book_author,
    'length': book_length,
})

df_books.to_csv('books.csv', index=False)
