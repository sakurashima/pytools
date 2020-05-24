import requests


url = 'https://www.bilibili.com'


headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
}


proxies = {
        'https':'https://117.87.177.50:9000',
}


params = {
    'keyword':'ER图',
}


response = requests.get(url, headers=headers)

print(response.status_code)

with open('repos.txt', 'w', encoding='utf-8') as f:
    f.write(response.text)
