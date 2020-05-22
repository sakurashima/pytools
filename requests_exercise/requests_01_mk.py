import requests


# r ====>  Response objetc
r = requests.get('https://www.bilibili.com')

"""
requests的方法不止一种，http请求都可以实现
r = requests.post()
r = requests.put()
r = requests.head()
r = requests.options()
...
"""

