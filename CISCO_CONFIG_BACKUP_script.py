import paramiko
import time
import os
from netmiko import ConnectHandler
ip_address = "100.100.100."
username = "cisco"
password = "cisco"

#define the object/ host for netmiko
local_asa = {
'device_type': 'cisco_asa',
'ip': '100.100.100.16',
'username': 'cisco',
'password': 'cisco',
'secret': 'cisco',
'verbose': False
}

#define the object/ host for netmiko
remote_asa = {
'device_type': 'cisco_asa',
'ip': '100.100.100.17',
'username': 'cisco',
'password': 'cisco',
'secret': 'cisco',
'verbose': False,
}




# function to back up non asa devices using parmiko libary
def cisco_backup_ios():
    remote_connection.send("en\n")
    time.sleep(1)
    remote_connection.send(password+'\n')
    time.sleep(1)
    remote_connection.send("copy running-config start\n")
    time.sleep(1)
    remote_connection.send("\n")
    time.sleep(1)
    remote_connection.send("copy running-config tftp:\n")
    time.sleep(1)
    remote_connection.send("100.100.100.1\n")
    time.sleep(1)
    remote_connection.send("\n")
    print("completed")

# function to back up non asa devices using NETMIKO libary
def cisco_backup_asa():

#connects to the specific node we have define above
    net_connect = ConnectHandler(**local_asa)

# puts us in enable mode
    net_connect.enable()

# sends the command via the netmiko libary and saves the output to a varible called output
    output = net_connect.send_command("show hostname")

    output = output.rstrip()
    path = ("/var/lib/tftpboot/")
    completepath = os.path.join (path,output)
    print (completepath)
    f = open(completepath, "w")
    output = net_connect.send_command("show run")

    f.write(output)
    f.close()
    print ()

    net_connect = ConnectHandler(**remote_asa)
    net_connect.enable()

    output = net_connect.send_command("show hostname")
    output = output.rstrip()
    path = ("/var/lib/tftpboot/")
    print ("/var/lib/tftpboot/")
    completepath = os.path.join (path, output)
    f = open("/var/lib/tftpboot/"+output,"w")
    output = net_connect.send_command("show run")
    f.write(output)
    f.close()
    print ()

#for the main nodes
for i in range (0,15):
 try:
  ssh_client = paramiko.SSHClient()
  ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  ssh_client.connect(hostname=ip_address+(str(i)),username=username,password=password)
  remote_connection = ssh_client.invoke_shell()
  cisco_backup_ios()
  print(ip_address+(str(i)),"completed")


 except:
  print("not connected")
  print(ip_address + (str(i)), "failed")

# for the asa's

cisco_backup_asa()

#for C in range (16,18):
# try:
  #ssh_client = paramiko.SSHClient()
  #ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  #ssh_client.connect(hostname=ip_address+(str(i)),username=username,password=password)
  #remote_connection = ssh_client.invoke_shell()

#  print(ip_address+(str(C)),"completed")


# except Exception as e:
#  print(e)
#  print("not connected")
#  print(ip_address + (str(i)), "failed")
