from bs4 import BeautifulSoup
import requests

ROOT = 'https://subslikescript.com/'

response = requests.get(f'{ROOT}movies')
content = response.text
soup = BeautifulSoup(content, 'lxml')

# pagination
pagination = soup.find('ul', class_='pagination')
pages = pagination.find_all('li', class_='page-item')
last_page = pages[-2].text

links = []

for page in range(1, int(last_page)+1):
    response = requests.get(f'{ROOT}movies_letter-A?page={page}')
    content = response.text
    soup = BeautifulSoup(content, 'lxml')

    box = soup.find('article', class_='main-article')

    links_box = box.find_all('a', href=True)  # 寻找标签中所有的有’herf‘的‘a'标签

    for link in links_box:
        links.append(ROOT + link['href']) # 获得每个标签中的链接

    for link in links:
        try:
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
        except:
            print('------- Link not working ---------')
            print(link)

        with open(title + '.txt', 'w', encoding="UTF-8") as file:
            file.write(transcript)

