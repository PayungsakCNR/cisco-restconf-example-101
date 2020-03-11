### RESTCONF Cisco CSR1000v ###
### Payungsak Klinchampa ###
### pao@paocloud.in.th ###

import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import os
from dotenv import load_dotenv

load_dotenv()
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

HOST='10.10.200.111'
PORT=443
USERNAME=os.getenv("USERNAME")
PASSWORD=os.getenv("PASSWORD")

def getData():
	urlGigEth = "https://{h}:{p}/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=1".format(h=HOST, p=PORT)
	urlHostname = "https://{h}:{p}/restconf/data/Cisco-IOS-XE-native:native/hostname".format(h=HOST, p=PORT)
	urlVersion = "https://{h}:{p}/restconf/data/Cisco-IOS-XE-native:native/version".format(h=HOST, p=PORT)
	headers = {
		'User-Agent': 'PaOCLOUD RESTCONF Client',
		'content-type': 'application/yang-data+json',
		'accept': 'application/yang-data+json'
	}

	try:
		 resultGigEth = requests.get(urlGigEth, auth=(USERNAME, PASSWORD),
                                headers=headers,timeout=5,verify=False)
		 resultHostname = requests.get(urlHostname, auth=(USERNAME, PASSWORD),
                                headers=headers,timeout=5,verify=False)
		 resultVersion = requests.get(urlVersion, auth=(USERNAME, PASSWORD),
                                headers=headers,timeout=5,verify=False)
		 print("###########################")
		 print("Hostname: " + resultHostname.json()['Cisco-IOS-XE-native:hostname'])
		 print("Version: " + resultVersion.json()['Cisco-IOS-XE-native:version'])
		 print("###########################" + '\n')
		 print("Interface: GigabitEthernet1")
		 print("IPv4 Address: " + resultGigEth.json()['Cisco-IOS-XE-native:GigabitEthernet']['ip']['address']['primary']['address'])
		 print("IPv6 Address: " + resultGigEth.json()['Cisco-IOS-XE-native:GigabitEthernet']['ipv6']['address']['prefix-list'][0]['prefix'])
		 print("IPv6 Link Local Address: " + resultGigEth.json()['Cisco-IOS-XE-native:GigabitEthernet']['ipv6']['address']['link-local-address'][0]['address'] + '\n')
	
	except Exception as e:
		print(e)

getData()