# Python3
import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#Specify Cisco vManage IP address (using URI), and uname and password
vmanage_ip = "sandboxsdwan.cisco.com"
username = "devnetuser"
password = "Cisco123!"

# Trying this with an f string first to make sure I have this down
base_url_str = (f"https://{vmanage_ip}:8443/")

#login API 

login_action = "j_security_check"
login_data = {"j_username": username, "j_password": password}

#Make a new variable to show full URI https://sandboxsdwan.cisco.com:8443/j_securtiy_check
login_url = base_url_str + login_action

# Establish a new session and connect to vManage
sess = requests.session()
# HTTP POST the URL and login data as a dictionary.
login_response = sess.post(url=login_url, data=login_data, verify=False)
device_resource = "dataservice/device"
# This piece takes the URL string and appends it with dataservice/device
device_url = base_url_str + device_resource
device_response = sess.get(device_url, verify=False)
device_items = json.loads(device_response.content)['data']
