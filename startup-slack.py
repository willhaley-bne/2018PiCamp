import requests
import os
import netifaces as ni
import json


with open('/home/pi/.config/aiy/device_name') as f:
    device_name = f.read()
f.close()

if os.path.exists('slack.txt') is False:
    raise Exception('You need to create a slack.txt file in this directory with the endpoint url')

with open('slack.txt') as f:
    url = f.read()
f.close()

ni.ifaddresses('wlan0')
ip = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']

message = {"text": "%s IP Address is %s" % (device_name, ip)}
r = requests.post(url, data=json.dumps(message))
