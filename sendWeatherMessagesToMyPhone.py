import os
from twilio.rest import Client
import json
import pprint
import requests
import datetime
import time

location = 'Shanghai'
# Download the JSON data from OpenWeatherMap.org's API
url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&APPID=1ffc6aad9bc3d5976d7beb8e6e455af2' % location
C = 273.15
messageBody = None


def sendMessage(messageBody):
    TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
    TO_NUMBER = os.getenv('TO_NUMBER')
    FROM_NUMBER = os.getenv('FROM_NUMBER')
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        client.api.account.messages.create(to=TO_NUMBER, from_=FROM_NUMBER, body=messageBody)
        print('Send message success!')
    except:
        print('Message failed to send!')


while True:
    time.sleep(60)
    now = datetime.datetime.now()
    if now.hour == 15 and now.minute == 25:
        try:
            responses = requests.get(url)
            responses.raise_for_status()
            print('Getting weather data for %s' % location)
            if responses.status_code == requests.codes.ok:
                weatherInfo = json.loads(responses.text)
                if weatherInfo['cod'] == 200:
                    # pprint.pprint(weatherInfo)
                    messageBody = '''城市:%s
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
                           weatherInfo['wind']['deg'], weatherInfo['wind']['speed'])

                    print(messageBody)
                    sendMessage(messageBody)
                    print('Get weather info for %s success!' % location)
                else:
                    print('Get weather info for % failed!' % location)
        except:
            print('Some error occured!')
