from bs4 import BeautifulSoup
import requests
import wget
import os
from urllib.parse import urlparse, parse_qs

url = input("enter url:")
t = urlparse(url)
d = parse_qs(t.query)

download_path = os.path.join('downloads/' + d['id'][0])

result = []
req = requests.get(url)
soup = BeautifulSoup(req.text, features="html.parser")

images = soup.find_all("img", {'border': 0})
if images:
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    for image in images:
        if '.gif' not in str(image):
            image_url = "http://www.coloring-book.info/coloring/" + image.get('src').replace('_m', '').replace('/thumbs', '')
            wget.download(image_url, download_path)
