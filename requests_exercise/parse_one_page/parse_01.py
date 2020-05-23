import requests
import re


def get_one_page(url):
    """爬取单个网页"""

    headers = {
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/53    7.36'
}
    r = requests.get(url, headers=headers, params={'keywords':'六学'}, timeout=0.5)
    
    # 如果不能正常访问，返回
    if r.status_code == 200:
        print('成功访问')
        return r.text
    else:
        return '访问异常'


def parse_one_page(url):
    """解析单个网站"""
    
    html = get_one_page(url)

    """
    content="bilibili是国内知名的视频弹幕网站，这里有最及时的动漫新番，最棒的ACG氛围，最有创意的Up主。大家可以在这里找到许多欢乐。
    """
    print(html)
    pattern = re.compile("content=\".*\"")
    

    items = re.findall(pattern, html)
    
    print(items)


def main():
    
    # 爬取网站网址host名
    url = 'https://search.bilibili.com/all?'

    parse_one_page(url)



if __name__ == '__main__':
    main()
