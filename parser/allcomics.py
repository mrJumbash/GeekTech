from pprint import pprint

import requests
from bs4 import BeautifulSoup

URL = "https://milftoon.xxx/"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0"
}


def get_html(url):
    req = requests.get(url, headers=HEADERS)
    return req

def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all("div", class_="col-6 col-md-4 badge-pos-1")
    comics = []
    for item in items:
        comic = {
            'title': item.find("div", class_="page-item-detail manga").find('a').get('title'),
            'link': item.find("div", class_="page-item-detail manga").find('a').get('href'),
            'photo': item.find("div", class_="page-item-detail manga").find('img').get('src'),
            'rate': item.find('div', class_='meta-item rating r-8muses').find('span').string

        }
        comics.append(comic)
    return comics

def parser():
    html = get_html(URL)
    if html.status_code == 200:
        comics = []
        for i in range(1, 2):
            html = get_html(f"{URL}page/{i}/")
            comic = get_data(html.text)
            comics.extend(comic)

        return comics
    else:
        raise Exception("Error in parser!")

