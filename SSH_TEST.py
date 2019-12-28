import paramiko
import time

ip_address = "100.100.100."
username = "cisco"
password = "cisco"

# for loop with defined range
for i in range (0,16):

#try the code in the below brackets
#try to connect via ssh to the current value of ipn address + i
 try:
  ssh_client = paramiko.SSHClient()
  ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  ssh_client.connect(hostname=ip_address+(str(i)),username=username,password=password)
  remote_connection = ssh_client.invoke_shell()
  # important sleep to allow for the connection to establish ;
  time.sleep(2)
  print ("connected to ", ip_address+(str(i)))

# for any error which is thrown catch it and print the line error connecting
 except:
  print("error conencting ", ip_address+(str(i)))
  # important sleep to allow time for current attempt to end
  time.sleep(2)