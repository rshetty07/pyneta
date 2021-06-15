from datetime import datetime
from netmiko import ConnectHandler
from getpass import getpass

start_time = datetime.now()
cisco = { 
    "host": 'cisco3.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_nxos',
#    "fast_cli": 'True',
}

net_connect = ConnectHandler(**cisco)
print(net_connect.find_prompt())

config = [
        'ip name-server 1.1.1.1',
        'ip name-server 1.0.0.1',
        'ip domain-lookup',
]
output = net_connect.send_config_set(config)

ping_output = net_connect.send_command("ping google.com")
if "!!" in ping_output:
    print("Ping Successful:")
    print("\n\nPing Output: {}\n\n".format(ping_output))
else:
    raise ValueError("\n\nPing Failed: {}\n\n".format(ping_output))
net_connect.disconnect()

end_time = datetime.now()
print("Total Execution Time: {}\n".format(end_time - start_time))
print (output)

