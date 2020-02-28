import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
# print(res.text)

soup =  BeautifulSoup(res.text, 'html.parser')
# print(soup)
print(soup.body)