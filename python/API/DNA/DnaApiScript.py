# Python 3
#! usr/bin/env Python

from dnacentersdk import api

# Create a DNA Center API connection object using the sandbox
DNAC = api.DNACenterAPI(username="devnetuser",
           password="Cisco123!",
           base_url="https://sandboxdnac2.cisco.com")

# Find all devices
DEVICES = DNAC.devices.get_device_list()

# Print select information about the retreived devices

print("{0:25s}{1:1}{2:45}{3:1}{4:15}".format("Device Name",
    "|", "Device Type", "|", "Up Time"))
print("-"*95)

for device in DEVICES.response:
    print("{0:25s}{1:1}{2:45}{3:1}{4:15}".format(device.hostname,
    "|", device.type, "|", device.upTime))

print("-"*95)
