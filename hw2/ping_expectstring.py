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
output = net_connect.send_command(command, expect_string=r"Protocol", strip_command=False, strip_prompt=False)

output += net_connect.send_command("\n", expect_string=r"Target", strip_command=False, strip_prompt=False)
output += net_connect.send_command("8.8.8.8", expect_string=r"Repeat", strip_command=False, strip_prompt=False)

output += net_connect.send_command("\n", expect_string=r"Datagram", strip_command=False, strip_prompt=False)
output += net_connect.send_command("\n", expect_string=r"Timeout", strip_command=False, strip_prompt=False)
output += net_connect.send_command("\n", expect_string=r"Extended", strip_command=False, strip_prompt=False)
output += net_connect.send_command("\n", expect_string=r"Sweep", strip_command=False, strip_prompt=False)
output += net_connect.send_command("\n", expect_string=r"#", strip_command=False, strip_prompt=False)

net_connect.disconnect()
print (output)

