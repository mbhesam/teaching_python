from paramiko import SSHClient , AutoAddPolicy
from time import sleep

def config_vlan(Connection,start_vlan,end_vlan):
    Connection.send("en \n")
    sleep(2.5)
    Connection.send("cisco \n")
    sleep(2.5)
    Connection.send("conf t \n")
    sleep(2.5)
    for i in range(start_vlan,end_vlan+1):
        Connection.send("vlan "+str(i)+"\n")
        sleep(2.5)
        Connection.send("name PY_VLAN"+str(i)+"\n")
        
ip = "192.168.30.1"
for i in range(15,21):
    session = SSHClient()
    session.set_missing_host_key_policy(AutoAddPolicy)
    session.connect(hostname=ip+str(i),username="kia",password="kia",
                look_for_keys=False,allow_agent=False)
    connection = session.invoke_shell()
    if i == 15 or i == 16 or i == 17:
        config_vlan(connection,5,20)
    elif i == 18:
        config_vlan(connection,5,10)
    elif i == 19:
        config_vlan(connection,11,15)
    elif i == 20:
        config_vlan(connection,16,20)
    connection.close()
