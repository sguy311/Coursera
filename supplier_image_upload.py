#!/usr/bin/env python3
import requests
import os
import re

path = "./supplier-data/images/"
url = "http://localhost/upload/"
ext = r"\d+.jpeg"
for files in os.listdir(path):
    if re.match(ext,files):
        file = os.path.join(path,files)
        with open(file, 'rb') as opened:
            r = requests.post(url, files={'file': opened})