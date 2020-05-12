import hashlib


def main():
    pwd = input('password:')
    md5 = hashlib.md5()
    md5.update(pwd.encode('utf-8'))
    print(md5.hexdigest())


if __name__ == '__main__':
    main()

