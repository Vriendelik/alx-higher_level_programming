#!/usr/bin/python3
import urllib.request

url = "https://alx-intranet.hbtn.io/status"

try:
    with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
except urllib.error.URLError as e:
    print("Error fetching URL:", e.reason)
