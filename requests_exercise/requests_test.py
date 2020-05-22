import requests


r = requests.get('https://api.github.com/repos/psf/requests')

words = r.json()
print(words)
