#!/usr/bin/env python3
"""
Sesion and prepped to change the paramethers
"""
from requests import Request, Session

url = "https://httpbin.org/get"

# INFO: Create a new session
s = Session()
headers = {"Custom-Header": "my_custom_header"}
# cookies = {"Coockies": "CustomCookie123"}

# INFO: the original request
req = Request("GET", url, headers=headers)

# INFO: Updating the url request with prepeed and changing the headers info
prepped = req.prepare()
prepped.headers["Custom-Header"] = "my_new_custom_header"

# INFO: Adding a new header
prepped.headers["AnOtherHeader"] = "Other_header"


# NOTE: USE send() method to send the request
response = s.send(prepped)

print(response.text)
