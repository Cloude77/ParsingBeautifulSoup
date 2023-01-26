import requests
from fake_useragent import UserAgent

ua = UserAgent()

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 OPR/94.0.0.0 (Edition Yx 03)"
# }

url = 'https://httpbin.org/headers'
# headers = {
#     "User-Agent": ua.random
# }
for i in range(1, 11):
    headers = {
        "User-Agent": ua.random
    }
    res = requests.get(url, headers=headers)
    print(res.json())
