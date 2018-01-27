import json
import pprint
import requests
import sys

if len(sys.argv) < 2:
    print('Usage: quickWeather location')
    sys.exit()
location = ' '.join(sys.argv[1:])
# Download the JSON data from OpenWeatherMap.org's API
url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&APPID=1ffc6aad9bc3d5976d7beb8e6e455af2' % location
C = 273.15
try:
    responses = requests.get(url)
    responses.raise_for_status()
    print('Getting weather data for %s' % location)
    if responses.status_code == requests.codes.ok:
        weatherInfo = json.loads(responses.text)
        if weatherInfo['cod'] == 200:
            # pprint.pprint(weatherInfo)
            print('''城市:%s
            温度:%.2f℃
            最高温:%.2f℃
            最低温:%.2f℃
            湿度:%d%%
            压力:%dhpa
            天气:%s
            风向:%d°
            风速:%dm/s
            ''' % (weatherInfo['name'], weatherInfo['main']['temp'] - C, weatherInfo['main']['temp_max'] - C,
                   weatherInfo['main']['temp_min'] - C, weatherInfo['main']['humidity'],
                   weatherInfo['main']['pressure'], weatherInfo['weather'][0]['description'],
                   weatherInfo['wind']['deg'], weatherInfo['wind']['speed']))
        else:
            print('获取天气信息失败！')
except:
    print('Some error occured!')
