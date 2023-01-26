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
