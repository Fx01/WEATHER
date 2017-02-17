from  bs4 import BeautifulSoup
import requests
import nexmo
import datetime
import time
KEY = 'd6d49ab2'
SECRET = '53237ba9dc8847f4'
URLSH = 'http://www.weather.com.cn/weather/101020100.shtml'

while True:
    if (datetime.datetime.now().hour != 7)  and (datetime.datetime.now().minute != 0):
        time.sleep(1)
    else:
        r = requests.get(URLSH)
        html = r.content
        soup = BeautifulSoup(html, 'html.parser')
        info_list = soup.find('ul', attrs={'class': 't clearfix'})
        day = info_list.find_all('h1')
        wea = info_list.find_all('p', attrs={'class': 'wea'})
        tem = info_list.find_all('p', attrs={'class': 'tem'})
        text = ''
        for a, b, c in zip(day, wea, tem):
            day = a.get_text()
            wea = b.get_text()
            tem = c.get_text()
            text = text + day + wea + tem + '\r'
        client = nexmo.Client(key=KEY, secret=SECRET)
        response = client.send_message({'from': 'Python', 'to': '8618767389415', 'text': text, 'type': 'unicode'})
