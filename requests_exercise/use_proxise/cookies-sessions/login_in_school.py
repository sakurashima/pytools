import requests



session = requests.session()

post_url = 'http://jxpt.ahu.edu.cn/meol/common/security/login.jsp'
post_data = {'IPT_LOGINUSERNAME':'G321312', 'IPT_LOGINPASSWORD':'q32132113'}
headers = {
       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}


# 使用session发送post请求，cookie保存在其中
session.post(post_url, data=post_data, headers=headers)

r = session.get('http://jxpt.ahu.edu.cn/meol/personal.do', headers=headers)

with open('zhihuishu.txt', 'w') as f:
    f.write(r.text)
