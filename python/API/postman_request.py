#Python3

# Short script to demonstrate the use of HTTP requests in a python script
# You need to install the 'requests' python extension for this to works
# from bash - 'pip3 install requests'

# First import requests
import requests
import json

# Then define the URL using a string
url = "https://postman-echo.com/get"

# Define your string for querying the server as a dictionary
querystring = {"test":"123"}

# Headers are blank for this example
headers = {}

# Response will equal the HTTP get
response = requests.request ("GET", url, headers=headers, params=querystring)
# Which i think becomes:
# GET https://postman-echo.com/get?test=123

print(response.text)
