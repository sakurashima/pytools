import requests



url = 'https://search.bilibili.com/all?'

headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}


response = requests.get(url, headers=headers, params={'keyword':'千面妖妇EX'}, timeout=1)

with open('demo.txt', 'w', encoding='utf-8') as f:
    f.write(response.text)

print('完成')
