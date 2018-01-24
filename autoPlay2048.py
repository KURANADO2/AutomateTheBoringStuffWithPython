from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome('D:\\Software\\chromedriver.exe')
browser.get('https://gabrielecirulli.github.io/2048/')
startEle = browser.find_element_by_css_selector('a[class="restart-button"]')
htmlEle = browser.find_element_by_tag_name('html')
gameMessEle = browser.find_element_by_css_selector('div[class="game-message"] > p')
# Start game
startEle.click()
while gameMessEle.text != 'Game over!':
    htmlEle.send_keys(Keys.UP)
    time.sleep(0.5)
    htmlEle.send_keys(Keys.RIGHT)
    time.sleep(0.5)
    htmlEle.send_keys(Keys.DOWN)
    time.sleep(0.5)
    htmlEle.send_keys(Keys.LEFT)
    time.sleep(0.5)
print('Sorry! Game over!')