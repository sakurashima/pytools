import hashlib


md5 = hashlib.md5()
md5.update('mysql1'.encode('utf-8'))
print(md5.hexdigest())
