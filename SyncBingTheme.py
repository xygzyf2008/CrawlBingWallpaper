# -*- coding: utf-8 -*-

# pip install requests
# pip install bs4

import requests
from bs4 import BeautifulSoup
import urllib.request
import datetime
import os

url = 'https://www.bing.com/'
folder = 'D:/1/bing theme/%s/' % datetime.datetime.now().year

if __name__ == '__main__':
    res = requests.get(url)  # Get方式获取网页数据
    soup = BeautifulSoup(res.text, 'html.parser')
    tag = url[:-1] + soup.select('#bgImgProgLoad')[0]['data-ultra-definition-src']
    fileName = datetime.datetime.now().strftime('%Y-%m-%d') + '.jpg'
    if not os.path.exists(folder):
        os.makedirs(folder)
    print(tag, '----------', fileName)
    local_filename = urllib.request.urlretrieve(tag, folder + fileName)
    print(local_filename)
