import json
from pprint import pprint

data = json.load(open("example.json"))

#pprint(data)

fN = data["address"]["city"]

phone_num = data["phoneNumbers"]
for i in phone_num:
    pprint(i)

pprint(data.keys())