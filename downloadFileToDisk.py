import requests
import os

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')

file = open('D:\\Python\\pg1112.txt', 'wb')

try:
    res.raise_for_status()
    print('downloading the file to pg1112.txt')
    for chuck in res.iter_content(100000):
        file.write(chuck)
except Exception as exc:
    print('There was a problem: %s' % exc)
file.close()

