#!/usr/bin/env python3

import os
from PIL import Image

path = "./supplier-data/images/"
print(path)
for files in os.listdir(path):
        if files == "README":
                continue
        elif files == "LICENSE":
                continue
        else: 
                print(files)
                split = files.split(".")
                print(split[0])
                name = "{}{}.jpeg".format(path,split[0])
                print(name) 
                im = Image.open(os.path.join(path,files)) 
                im.resize((600,400)).convert("RGB").save(name) 