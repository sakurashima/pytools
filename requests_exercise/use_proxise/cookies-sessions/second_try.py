import requests



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'Cookie':'dshdjahdjadhjhdjahdjhadkjhjkdshjkahdjkha5E1DB38.TM1',
}

url = 'http://jxpt.ahu.edu.cn/meol/personal.do'

r = requests.get(url, headers=headers)

with open('html2.txt', 'w') as f:
    f.write(r.text)
