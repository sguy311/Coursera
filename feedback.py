#!/usr/bin/env python3

import os
import json
import collections

#feedback = 
files = os.listdir("feedback")
for file in files:
	entry = collections.OrderedDict()
	path = os.path.join("feedback/", file)
	print(path)
	with open(path, 'r') as f:
		lines = f.readlines()
		entry['title'] = lines[0].strip("[\n]")
		entry['name'] = lines[1].strip("[\n]")
		entry['date'] = lines[2].strip("[\n]")
		entry['remarks'] = lines[3].strip("[\n]")
		print(entry)
		feedback_json = json.dumps(entry)
		print(feedback_json)





