#!/usr/bin/env python3

import requests

url = "https://httpbin.org/post"


my_file = {"archivo": open("my_file.txt", "r")}

response = requests.post(url, files=my_file)
print(response.text)
