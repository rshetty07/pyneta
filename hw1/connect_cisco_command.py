from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "host": 'cisco4.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_ios',
}
 
net_connect = ConnectHandler(**device1)
version = net_connect.send_command("show version")
f = open("show_version.txt", 'w')
print(version, file=f)

