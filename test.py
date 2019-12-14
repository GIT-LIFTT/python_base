import paramiko
import time
ip_address = "100.100.100.3"
username = "cisco"
password = "cisco"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)
print ("connected to ", ip_address)

time.sleep(100)

print ("testing")
