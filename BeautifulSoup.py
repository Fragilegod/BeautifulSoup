import requests
from bs4 import BeautifulSoup


def getting_posts(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.find_all('div', {'data-adaptive': '1'})

    posts = []

    for item in items:
        try:
            date = item.find('span', {'class':'name'}).get('title')
        except AttributeError:
            date = ''
        try:
            author = item.find('p', {'class': 'name'}).text
        except AttributeError:
            author = ''
        try:
            title = item.find('div', {'class':'caption'}).find('h3').text
        except AttributeError:
            title = ''
        try:
            subtitle = item.find('p', {'class':'subtitle'}).text
        except AttributeError:
            subtitle = ''
        try:
            anounce = item.find('div', {'class':'lead'}).find('p').text
        except AttributeError:
            anounce = ''

        posts.append({'date': date,
                   'author': author,
                   'title': title,
                    'subtitle': subtitle,
                   'anounce': anounce})
    return posts




url = 'https://nplus1.ru/'
posts = getting_posts(url)
print(posts)
