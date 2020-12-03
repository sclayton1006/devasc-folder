# Python3

from meraki_sdk.meraki_sdk_client import MerakiSdkClient

# Define your parameters
X_CISCO_MERAKI_API_KEY = "15da0c6ffff295f16267f88f98694cf29a86ed87"

#Build a new client connection to the Meraki REST API
meraki = MerakiSdkClient(X_CISCO_MERAKI_API_KEY)

# Get a list of all organisations for account 'DevNet' and place them in 'orgs'
orgs = meraki.organizations.get_organizations()
for org in orgs:
    print("Org ID: {} and Org Name: {}".format(org['id'], org['name']))

params = {}
params['organization_id'] = "549236" # DevNet Sandbox

# Get a list of all the network for the Cisco DevNet organisation
nets = meraki.networks.get_organization_networks(params)
for net in nets:
    print("Network ID: {0:20s}, Name: {1:45s}, Tags: {2:<10s}".format(net['id'], net['name'], str(net['tags'])))

