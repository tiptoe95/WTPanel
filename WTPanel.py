

import requests
from bs4 import BeautifulSoup
import json
import time


refresh_rate = 0.1
url_indicators = r'http://127.0.0.1:8111/indicators'


def get_json(url):
    html = requests.get(url)
    parsed_html = BeautifulSoup(html.text, features='lxml')
    data = json.loads(parsed_html.get_text())
    return data


if __name__ == '__main__':
    i = 0
    while i < 100:
        data_indicators = get_json(url_indicators)
        altitude = data_indicators['altitude_hour']
        print(f"{altitude:.1f} m")
        time.sleep(refresh_rate)
