#!/usr/bin/python3

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.getheader('X-Request-Id')
            print(x_request_id)
    except urllib.error.URLError as e:
        print("Error fetching URL:", e.reason)
