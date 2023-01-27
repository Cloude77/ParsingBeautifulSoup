import re

from bs4 import BeautifulSoup

# soup = BeautifulSoup('<a></b></a>', 'lxml')
# print(soup)

with open('html/page.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')

# print(soup)
# print(soup.a)  # <a class="link-secondary" href="#"> Subscribe </a>
# print(soup.title)  # <a class="link-secondary" href="#"> Subscribe </a>

# title = soup.title
# print(title)
# print(title.text)
# print(title.get_text())  # method
# print(title.string)

h1 = soup.h1
# print(h1)
# print(h1.attrs)  # {'class': ['display-4', 'fst-italic'], 'id': 'h1-title'}
# print(h1.attrs['id'])  # h1-title
# print(h1.get('id2'))  # None  without mistakes
print(h1.has_attr('id2'))  # False

print(h1.text.strip())  # Title of a  longer   featured blog post

print(h1.get_text(strip=True))  # Title of alongerfeatured blog post
print(h1.get_text(strip=True, separator=' '))  # Title of a longer featured blog post
print(soup.find('a'))  # <a class="link-secondary" href="#"> Subscribe </a>

# links = soup.find_all('a')   #  [<a class="link-secondary" href="#"> Subscribe </a>, <a class="blog-header-logo text-dark
# print(links)

print(soup.find('nav').find('a').text)  # World
print(soup.find('nav').find('a').get('href'))  # #

links = soup.find('nav').find_all('a')
print(len(links))  # 12

for link in links:
    print(f'{link.get_text(strip=True)} - {link.get("href")}')  # spaces World - # U.S. - #

links = soup.find('nav').find_all('a', class_='p-2')  # <a class="p-2 link-secondary
links = soup.find('nav').find_all('a', class_='p-2 link-secondary active')
links = soup.find('nav').find_all('a', {'class': 'p-2 link-secondary'})  # <a class="p-2 link-secondary"

links = soup.find('nav').find_all('a', attrs={'class': 'p-2 link-secondary', "data-link": "link"})

links = soup.find('nav').find_all('a', attrs={'id': 'design'})
links = soup.find('nav').find_all(id='design')  # [<a class="p-2 link-secondary" href="#" id="design">Design</a>]

links = soup.find('nav').find_all(title='test')  # <a class="p-2 link-secondary" href="#" title="test">Technology</a>]
print(links)

print(end='===============================================================\n')  # <h1 class="display-4

print(soup.find('h1'))
# print(soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5']))


print(soup.find_all(re.compile('^h[1-6]')))  # h1 - h3


print(soup.find_all(True))  # the whole list(all)