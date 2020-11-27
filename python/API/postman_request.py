#Python3

# Short script to demonstrate the use of HTTP requests in a python script
# You need to install the 'requests' python extension for this to works
# from bash - 'pip3 install requests'

# First import requests
import requests
import time

# Then define the URL using a string
url = "https://postman-echo.com/get"
method = "GET"
# Define your string for querying the server as a dictionary
querystring = {"test":"123"}

# Headers are blank for this example
headers = {}

# Comfort messaging, letting the user know something is happeneing. In
# production this would not have a 1 second wait in it.
print(f"Sending {method}. Please wait...\n\n")
time.sleep(1)

# Response will equal the HTTP get
response = requests.request (method, url, headers=headers, params=querystring)
# Which i think becomes:
# GET https://postman-echo.com/get?test=123
if response != "":
    # A bit of ASCII art for kicks...
    print("                                \n\
,---.                              |       \n\
`---..   .,---.,---.,---.,---.,---.|       \n\
    ||   ||    |    |---'`---.`---.        \n\
`---'`---'`---'`---'`---'`---'`---'o       \n\
                                    ")
    print(f"The {method} request was successful. The results are below:\n\n\
{response.text}")
else:
    print("API error. There is no data in the variable.")
