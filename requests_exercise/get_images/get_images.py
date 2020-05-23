import requests



response = requests.get('https://i0.hdslb.com/bfs/archive/f2649dfa6af9cec8976f0237c4772eb60cdcfd5f.png')

with open('bilibili_logo.png', 'wb') as f:
    f.write(response.content)



