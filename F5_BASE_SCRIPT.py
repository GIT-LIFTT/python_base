import paramiko
import time
ip_address = "100.100.100.15"
username = "root"
password = "default"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)
remote_connection = ssh_client.invoke_shell()

remote_connection.send("tmsh\n")
time.sleep(1)
remote_connection.send("list ltm\n")
time.sleep(1)
output = remote_connection.recv(1)
print ("connected to ", ip_address)
print (output.decode())
time.sleep(1)

print ("testing")
