import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 OPR/94.0.0.0 (Edition Yx 03)"
}

url = 'https://www.shutterstock.com/shutterstock/photos/1889118883/display_1500/stock-photo-funny-large-longhair-gray' \
      '-kitten-with-beautiful-big-blue-eyes-lying-on-white-table-lovely-fluffy-1889118883.jpg'

r = requests.get(url, headers=headers)

# Option 1
# in parts
with open('1.jpg', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=1024 * 10):  # number of bytes
        fd.write(chunk)
        print('Write chunk 10Kb')

# Option 2
# whole file
# with open('2.jpg', 'wb') as fd:
#     fd.write(r.content)
