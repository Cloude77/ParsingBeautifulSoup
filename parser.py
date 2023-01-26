import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 OPR/94.0.0.0 (Edition Yx 03)"
}

# https://www.youtube.com/watch?v=0acqq6ChCIs

query = {
    "v": "v=0acqq6ChCIs"
}

# # r = requests.get('http://httpbin.org/get', headers=headers)
# r = requests.get('https://www.youtube.com/watch', headers=headers, params=query)
#
# print(r.headers)
# print(r.text)
data = {

    "custemail": "sergey@gmail.com",
    "custname": "Sergey",
    "custtel": "8904769923",
    "comments": "Test request..."
}

r = requests.post('http://httpbin.org/post', headers=headers, data=data)

print(r.json()['form']['custemail'])
