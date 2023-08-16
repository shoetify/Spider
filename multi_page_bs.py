from bs4 import BeautifulSoup
import requests

ROOT = 'https://subslikescript.com/'

website = f'{ROOT}movies'
response = requests.get(website)
content = response.text

soup = BeautifulSoup(content, 'lxml')
box = soup.find('article', class_='main-article')

links_box = box.find_all('a', href=True)  # 寻找标签中所有的有’herf‘的‘a'标签
links = []
for link in links_box:
    links.append(ROOT + link['href']) # 获得每个标签中的链接

for link in links:
    response = requests.get(link)
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

