#!/usr/bin/env python3

import shutil
import psutil
import os
import subprocess
import email.message
import smtplib

def generate_error_report(sender, recipient, subject, body):
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    return message

def send(message):
    """Sends the message to the configured SMTP server."""
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()

    

def check_cpu():
    cpu = psutil.cpu_percent(0.1)
    return cpu 


def check_diskspace(drive):
    du = shutil.disk_usage(drive)
    return du

def check_memory():
    mem = psutil.virtual_memory()
    return mem

def check_connection():
    ping = subprocess.run(['ping','-c', '1', '127.0.0.1'], stdout=subprocess.DEVNULL)
    return ping.returncode

def all_checks():
    sender = "automation@example.com"
    recipient = "{}@example.com".format(os.environ.get('USER'))
    body = " Please check your system and resolve the issue as soon as possible."
    chkcpu = int(check_cpu())
    #print(chkcpu)
    if chkcpu > 90.0:
        #print("High CPU")
        subject = "Error - CPU usage is over 80%"
        email = generate_error_report(sender, recipient, subject, body)
        send(email)

    else:
        print("CPU Good")    
    ds = check_diskspace("/")
    dstotal = ds[0]
    dsfree = ds[2]
    #print(dsfree, dstotal)
    dspercent = int((dsfree/dstotal) * 100)
    #print(dspercent)
    if dspercent > 20:
        print("Free Space Good")
    else:
        #print*("Free Space Low")
        subject = "Error - Available disk space is less than 20%"
        email = generate_error_report(sender, recipient, subject, body)
        send(email)
    chkmem = check_memory()
    memfree = int(chkmem[1] /1000000)
    #print(memfree)
    if memfree > 500:
        print("Free Memory Good")
    else:
        subject = "Free Memory Low"
        email = generate_error_report(sender, recipient, subject, body)
        send(email)  
    net = check_connection()
    if net == 0:
        print("Network is Good")
    else:
        subject = "Network Issues"
        email = generate_error_report(sender, recipient, subject, body)
        send(email)




all_checks()


