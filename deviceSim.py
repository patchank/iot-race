import ibmiotf.device
import time
import sys

options = {
    "org": "vcj3bj",
    "type": "bike",
    "id": "dos",
    "auth-method": "token",
    "auth-token": "N7-4CBaCzUPO9LDaLJ"
}

# use: python deviceSim.py <lane> <times>

client = ibmiotf.device.Client(options)
client.connect()

myData={'bikeID':sys.argv[1]}

for x in range(int(sys.argv[2])):
    client.publishEvent(event="pedal", msgFormat="json", data=myData)
    print x
    time.sleep(0.25)
print "fin"