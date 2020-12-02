# Python 3

import json
import requests

""" URL parameters are build first """

url = "https://api.exchangeratesapi.io/latest?base=GBP"
method = "GET"
version = "HTTP/1.1"

""" HTTP GET rates against GBP and load string into a json variable """

webPull = requests.request("GET", url, headers="", params=version)
results = json.loads(webPull.text)

""" Query the disctionary and extract the USD rate, take away 0.02 and round to 2 decimal places"""

calVersion = results['rates']['USD'] - 0.02
cleanVersion = "{:.2f}".format(calVersion)

""" print the result """

print (f"========================================================\n\
The USD exchange rate minus 2 points is {cleanVersion}\n\
========================================================")
