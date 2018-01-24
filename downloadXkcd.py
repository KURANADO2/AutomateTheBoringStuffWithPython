#! python3
import requests
import os
import bs4


def downloadComic(folder):
    os.makedirs(folder, exist_ok=True)
    url = 'https://xkcd.com'
    while not url.endswith('#'):
        res = requests.get(url)
        try:
            res.raise_for_status()
            soup = bs4.BeautifulSoup(res.text, 'html.parser')
            comicEle = soup.select('#comic img')
            if comicEle == []:
                print('Could not find comic image!')
            else:
                comicUrl = comicEle[0].get('src')
                print('Downloading file: %s' % comicUrl)
                res2 = requests.get('http:' + comicUrl)
                try:
                    res2.raise_for_status()
                    imageFile = open(os.path.join(folder, os.path.basename(comicUrl)), 'wb')
                    for chuck in res2.iter_content(100000):
                        imageFile.write(chuck)
                    imageFile.close()
                    print('Download file: %s completed!' % comicUrl, end='\n\n')
                except Exception as exc2:
                    print('Download %s error' % comicUrl)
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'https://xkcd.com' + prevLink.get('href')
        except Exception as exc:
            print('Download error! Please try again later! %s' % exc)
    print('Done!')


downloadComic('D:\\Python\\XKCD')
