#!/usr/bin/env python3

import os
import json
import collections
import requests

#feedback =
url = "http://104.154.111.6/fruits/"
files = os.listdir("./supplier-data/descriptions/")
for file in files:
        entry = collections.OrderedDict()
        path = os.path.join("./supplier-data/descriptions/", file)
        print(path)
        name = file.split('.')
        
        with open(path, 'r') as f:
                lines = f.readlines()
                entry['name'] = lines[0].strip("[\n]")
                entry['weight'] = int(lines[1].strip("[ lbs][\n]"))
                entry['description'] = lines[2].strip("[\n]")
                entry['image name'] = "{}.jpeg".format(name[0])
                print(entry)
                feedback_json = json.dumps(entry)
                print(feedback_json)
                response = requests.post(url,json=feedback_json)
                response.raise_for_status()
