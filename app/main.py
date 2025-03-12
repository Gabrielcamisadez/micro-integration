from config import GLPI_URL, GLPI_TOKEN, NETBOX_TOKEN, NETBOX_URL, GLPI_SESSION_TOKEN
import urllib3
import json
import rich

urllib3.disable_warnings()


glpi_headers = {
    "Authorization": f"Basic Z2xwaTpnbHBp",
    "Content-Type": "application/json",
    "App-Token": GLPI_TOKEN,
    "Session-Token": GLPI_SESSION_TOKEN
}
class GLPI():
    def __init__(self):
        self.url = GLPI_URL
        self.token = GLPI_TOKEN

    def get_init_session(self):
        import requests
        url = "http://localhost:9090/apirest.php/initSession"
        r1 = requests.get(url, headers=glpi_headers, verify=False)
        print(r1.text)

    def get_device(self):
        import requests
        r1 = requests.get(self.url, headers=glpi_headers, verify=False)
        response = r1.json()

        if isinstance(response, list):
            for device in response:
                device.pop("links")
                rich.print(device)

# -----------------------------------------------------------------------------

netbox_headers = {
    "Authorization": f"Token {NETBOX_TOKEN}",
    "Content-Type": "application/json"
}

class NETBOX():
    def __init__(self):
        self.url = NETBOX_URL
        self.token = NETBOX_TOKEN

    def get_device(self):
        import requests 
        r1 = requests.get(self.url, headers=netbox_headers, verify=False)
        response = r1.json()
    
        if isinstance(response, dict):
            for device in response["results"]:
                rich.print(device["name"])



                

n = NETBOX()
n.get_device()        

g = GLPI()        
# g.get_init_session()
# g.get_device()