import requests
from bs4 import BeautifulSoup


def badgefetcher(url):
     req = requests.get(url)
     soup = BeautifulSoup(req.content, 'html.parser')
     #print(soup.find_all('div'))
     name = soup.find('h1', class_ = 'ac-heading ac-heading--badge-name-hero')
     allbadges = soup.find_all('div', class_='cr-standard-grid-item-content__title')
     badges = []
     for badge in allbadges:
          badges.append(badge.text.strip())
     return badges