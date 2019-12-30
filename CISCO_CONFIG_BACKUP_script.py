import paramiko
import time
ip_address = "100.100.100."
username = "cisco"
password = "cisco"

def cisco_backup():
    remote_connection.send("en\n")
    time.sleep(1)
    remote_connection.send(password+'\n')
    time.sleep(1)
    remote_connection.send("copy running-config tftp:\n")
    time.sleep(1)
    remote_connection.send("100.100.100.1\n")
    time.sleep(1)
    remote_connection.send("\n")
    print("end of function")

for i in range (0,15):
 try:
  ssh_client = paramiko.SSHClient()
  ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  ssh_client.connect(hostname=ip_address+(str(i)),username=username,password=password)
  remote_connection = ssh_client.invoke_shell()
  cisco_backup()
  print(ip_address+(str(i)),"completed")



 except:
  #print("not connected")
  print(ip_address + (str(i)), "failed")
