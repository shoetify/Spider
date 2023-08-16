from bs4 import BeautifulSoup
import requests

# Get the website content
website = 'https://subslikescript.com/movie/Titanic-120338'
response = requests.get(website)
content = response.text

# Using Beautiful soup to analysis
soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())

box = soup.find('article', class_='main-article')
# generate a box of this tag

title = box.find('h1').get_text()
# continue exploring in the box

transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

with open(title + '.txt', 'w', encoding="UTF-8") as file:
    file.write(transcript)
