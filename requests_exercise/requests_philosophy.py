import requests


r = requests.get('https://api.github.com/repos/psf/requests')

word = r.json()['description']
print('Remember this: {} '.format(word))
