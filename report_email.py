#!/usr/bin/env python3

import datetime
import os
import sys
import json

#path = "./supplier-data/descriptions/"
path = 'C:\\Users\\seang\\Documents\\007.txt'
data = {}
def load_data(filename):
    """Loads the contents of filename as a JSON file."""
    with open(filename) as file:
        lines = file.readlines()
        data['name'] = lines[0].strip("[\n]")
        data['weight'] = lines[1].strip("[\n]")
    return data

def process_data():
    pass

def main():
    pdfdata = load_data(path)
    print(pdfdata)

if __name__ == "__main__":
    main()