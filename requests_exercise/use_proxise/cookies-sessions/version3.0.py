import requests



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
}

Cookie = '#WRSESSI###TDAi####szeOcxNTD50n; JSE###21F1####E43A###91.TM1'

url = 'http://jxpt.ahu.edu.cn/meol/personal.do'

# for i in Cookie.split("; "):
#     print(i.split("=")[0], i.split("=")[1])

cookies = {i.split("=")[0]:i.split("=")[1]  for i in Cookie.split("; ")}
print(cookies)
r = requests.get(url, headers=headers, cookies=cookies)

with open('html2.txt', 'w') as f:
    f.write(r.text)
