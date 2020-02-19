from netmiko import Netmiko
from getpass import getpass

cisco1 = {
    "host": "100.100.100.17",
    "username": "cisco",
    "password": "cisco",
    "device_type": "cisco_asa",
}

net_connect = Netmiko(**cisco1)
command = "show hostname"

print()
print(net_connect.find_prompt())
output = net_connect.send_command(command)
net_connect.disconnect()
print(output)
print()