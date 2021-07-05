import json
from pprint import pprint

filename = "arista_arp.json"
with open(filename) as f:
    arp_data = json.load(f)

arp_dict = {}
arp_entries = arp_data["ipV4Neighbors"]

print()
print(arp_entries)
print()

for entry in arp_entries:
    ip_addr = entry["address"]
    mac_addr = entry["hwAddress"]
    arp_dict[ip_addr] = mac_addr
    print(arp_dict)

print()
pprint(arp_dict)
print()
