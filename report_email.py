#!/usr/bin/env python3
import reports
import datetime
import os
import sys
import json
import collections
import noemail

path = "/home/godsack/supplier-data/descriptions/"
files = os.listdir(path)
#print(files)
data = {}
date = datetime.datetime.now()
title = "Processed Update on {}".format(date.strftime("%B %d %Y"))
print(title)
sender = "automation@example.com"
recipient = "{}@example.com".format(os.environ.get('USER'))
subject = "Upload Completed - Online Fruit Store"
body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
def load_data(filename):
    """Loads the contents of filename as a JSON file."""
    #entry = {}
    for object in filename:
        #print(object)
        id = object.split('.')
        txt = os.path.join(path,object)
        #print(txt)
        with open(txt, 'r') as item:
            lines = item.readlines()
            #print(lines)
            data[id[0]] = {}
            data[id[0]]['name'] = lines[0].strip("[\n]")
            data[id[0]]['weight'] = lines[1].strip("[\n]")
    return data

def fruit_dict_to_table(car_data):
    print(car_data)
    """Turns the data in car_data into a list of lists."""
    table_data = []
    for item in car_data:
        #print(item)
        tname = "Name: {}".format(car_data[item]['name'])
        tweight = "Weight: {}".format(car_data[item]['weight'])
        table_data.append([tname])
        table_data.append([tweight])
        table_data.append("\n")
        #table_data.append([car_data[item]["name"], car_data[item]["weight"]])
    return table_data 

def process_data():
    pass

def main():
    #for file in files:
    pdfdata = load_data(files)
    #print(pdfdata)
    table = fruit_dict_to_table(pdfdata)
    print(table)
    reports.generate_report("/tmp/processed.pdf",title,table)
    email = noemail.generate_email(sender,recipient,subject,body,"/tmp/processed.pdf")


if __name__ == "__main__":
    main()