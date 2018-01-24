import bs4
import requests
import webbrowser
import sys

res = requests.get('https://www.baidu.com/s?wd=' + ' '.join(sys.argv[1:]))
try:
    res.raise_for_status()
    print(res.text)
except Exception as exce:
    print('There was a problem:' + exce)

soup = bs4.BeautifulSoup(res.text, 'html.parser')
linkElements = soup.select('.t a')
numOpen = min(5, len(linkElements))
for i in range(numOpen):
    webbrowser.open(linkElements[i].get('href'))
