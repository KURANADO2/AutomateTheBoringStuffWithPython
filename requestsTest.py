import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112-images.html')
try:
    res.raise_for_status()
    if res.status_code == requests.codes.ok:
        print(len(res.text))
        print(res.text[:2000])
except Exception as exc:
    # 如果try语句块中没有调用res.raise_for_status()，则当发生异常时，下面这条print语句将不会打印出任何内容
    print('There was a problem: %s' %exc)