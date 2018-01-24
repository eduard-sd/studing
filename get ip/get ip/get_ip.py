#install new module
#open cmd
#pip install "example:" requests

import requests 
def get_location():
    return requests.get("https://freegeoip.net/json/").json()

print (get_location())