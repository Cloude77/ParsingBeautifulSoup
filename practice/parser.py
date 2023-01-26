import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 OPR/94.0.0.0 (Edition Yx 03)"
}

url = 'https://www.shutterstock.com/shutterstock/videos/1041982291/preview/stock' \
      '-footage-a-girl-is-snowboarding-in-the-backcountry-during-the-winter-in-swiss-alps-shot-in-k-with-a-gimbal.webm'

r = requests.get(url, headers=headers, stream=True)
# print(r)
# print(r.content)
# print(r.raw.read(10))

with open('1.webm', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=1024 * 100):  # number of bytes
        fd.write(chunk)
        print('Write chunk 100Kb')
