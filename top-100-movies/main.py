import requests
from bs4 import BeautifulSoup

URL = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'
FILE = 'top-100-movies.txt'

def get_index(title):
    if ')' in title:
        splitted = title.split(')')
    else:
        splitted = title.split(':')

    index = int(splitted[0])
    return index


response = requests.get(URL)
web_page = response.text
soup = BeautifulSoup(web_page, 'html.parser')
titles = [title.get_text() for title in soup.find_all(name='h3', class_='title')]
print(titles)
# Hard way of reversing it:
# titles.sort(key=get_index)
# Easy way of reversing it
titles = titles[::-1]
print(titles)
# dates = [date.get_text() for date in soup.select('p strong')]
# print(dates)
with open(FILE, 'w') as file:
    file.write('\n'.join(titles))
