from MerakiDevNetID import getMerakiSandboxId as orgId
import requests
import json

ident = orgId()
url = (f"https://n149.meraki.com/api/v1/organizations/{ident}/networks")
headers = {'X-Cisco-Meraki-API-Key': "6bec40cf957de430a6f1f2baa056b99a4fac9ea0",
           'Accept': "application/json"}

apiCall = requests.request("GET", url, headers=headers)
apiClean = json.loads(apiCall.content)
#print(apiClean)

for net in apiClean:
    if net['organizationID'] == ident:
        print(f"The network ID is: {net['id']}")

#print(apiCall.text)
