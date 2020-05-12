import hashlib


db = {
        'qiankun':'1813acbcf435f129214a34a03f373cfe',
        'zhaoyutong':'tontong123',
}

def main():

    while True:

        # 确认用户名有效
        user_name = input('enter your username:')
        
        pwd = input('enter your password:')
        
        try:
            pop_user_name =  db[user_name]
        except KeyError as ret:
            print('用户名不存在\n')
        else:
            md5 = hashlib.md5()
            md5.update(pwd.encode('utf-8'))

            # 如果加密之后的字符串和从数据库里面提取出来的相同，那么放行
            if md5.hexdigest() == pop_user_name:
                print('请耐心等待两秒，稍后网页会自动跳转')
                break

            else:
                print('账户或密码错误，请重试\n')


if __name__ == '__main__':
    main()
