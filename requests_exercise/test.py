import requests
import time
import urllib


start_time = time.time()



# url = 'https://search.bilibili.com/all?' + urllib.parse.urlencode({'keyword':'六学'})
url = 'https://search.bilibili.com/all?' 
headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}


r = requests.get(url, headers=headers, params={'keyword':'崩坏三'}, timeout=1)




with open('bb_doc.txt', 'w', encoding='utf-8') as f:
    f.write(r.text)




over_time = time.time()
print('完成！运行时间：{:.2f}'.format(over_time-start_time))


