import os
from netmiko import ConnectHandler
from getpass import getpass

device1 = { 
    "host": 'cisco4.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_ios',
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

command = 'ping'
output = net_connect.send_command_timing(command)
output += net_connect.send_command_timing("\n")
output += net_connect.send_command_timing('8.8.8.8')
output += net_connect.send_command_timing("\n")
output += net_connect.send_command_timing("\n")
output += net_connect.send_command_timing("\n")
output += net_connect.send_command_timing("\n")
output += net_connect.send_command_timing("\n")
net_connect.disconnect()

print (output)

