from datetime import datetime
from netmiko import ConnectHandler
from getpass import getpass

nxos = { 
    "host": 'nxos2.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_nxos',
#    "global_delay_factor": 2,
}

net_connect = ConnectHandler(**nxos)
print(net_connect.find_prompt())

command = 'show lldp neighbors detail'
start_time = datetime.now()
#net_connect.send_command_timing(command)
net_connect.send_command_timing(command, delay_factor=20)
end_time = datetime.now()
net_connect.disconnect()

#print (output)
print("\n\nExecution Time: {}".format(end_time - start_time))

