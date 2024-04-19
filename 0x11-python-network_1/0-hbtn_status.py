#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status
and displays the body of the response in a specific format.
"""

import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body.decode("utf-8")))
