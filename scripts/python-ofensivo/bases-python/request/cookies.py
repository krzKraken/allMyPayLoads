#!/usr/bin/env python3


# INFO: using endpoint 'https://httpbin.org/cookies'

import requests

url = "https://httpbin.org/cookies"
cookies = dict(my_cookie="valorCookie")
response = requests.get(url=url, cookies=cookies)
print(response.text)
