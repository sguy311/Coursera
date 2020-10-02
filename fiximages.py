#!/usr/bin/env python3

import os
from PIL import Image
path = "./images"

for files in os.listdir(path):
	if files != ".DS_Store":
		print(files)
		name = f"/opt/icons/fixed_{files}.jpg"
		print(name)
		im = Image.open(os.path.join(path,files))
		im.rotate(270).resize((128,128)).convert("RGB").save(name)
