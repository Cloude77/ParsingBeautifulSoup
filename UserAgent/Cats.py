import requests
from fake_useragent import UserAgent

ua = UserAgent()


url = 'https://www.shutterstock.com/shutterstock/photos/1889118883/display_1500/stock-photo-funny-large-longhair-gray' \
      '-kitten-with-beautiful-big-blue-eyes-lying-on-white-table-lovely-fluffy-1889118883.jpg'


# print(url.split('/')[-1])  # last element

def get_name(file_url):
    return file_url.split('/')[-1]


r = requests.get(url, headers={"User-Agent": ua.random})

with open(get_name(url), 'wb') as fd:
    fd.write(r.content)
