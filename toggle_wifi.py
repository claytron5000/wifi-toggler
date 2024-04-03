from fabric import Connection, transfer
import os

interfaceName = "eth2"
def toggle_wifi(tog: bool):
    c = Connection(host="ubnt@192.168.1.1", connect_kwargs={"password": os.environ['PWD']})
    t = transfer.Transfer(c)
    if tog:
        stringCommand = "chmod +x ./turn-on-wifi.bash && ./turn-on-wifi.bash %s" % (interfaceName)
        print(stringCommand)
        t.put("turn-on-wifi.bash")
        c.run(stringCommand)
    else:
        stringCommand = "chmod +x ./turn-off-wifi.bash && ./turn-off-wifi.bash %s" % (interfaceName)
        print(stringCommand)
        t.put("turn-off-wifi.bash")
        c.run(stringCommand)        

def toggle_wifi2(time):
    c = Connection(host="ubnt@192.168.1.1", connect_kwargs={"password": os.environ['PWD']})
    t = transfer.Transfer(c)
    stringCommand = "chmod +x ./timed-turn-off-on.bash && ./timed-turn-off-on.bash %s %s" % (interfaceName, time+"m")
    print(stringCommand)
    t.put("turn-on-wifi.bash")
    c.run(stringCommand)
    
    