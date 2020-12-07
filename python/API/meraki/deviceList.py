from MerakiDevNetID import getMerakiSandboxId as orgId
import requests
import json

ident = orgId()
url = (f"https://n149.meraki.com/api/v0/organizations/{ident}/networks")
headers = {'X-Cisco-Meraki-API-Key': "6bec40cf957de430a6f1f2baa056b99a4fac9ea0",
           'Accept': "application/json"}

apiCall = requests.request("GET", url, headers=headers)
apiClean = json.loads(apiCall.text)

#print(apiCall.json())
n = 0
for element in apiClean:
    print (element['id'])
    n += 1