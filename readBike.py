import RPi.GPIO as GPIO
import time
import ibmiotf.device

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN)

options = {
    "org": "vcj3bj",
    "type": "bike",
    "id": "dos",
    "auth-method": "token",
    "auth-token": "N7-4CBaCzUPO9LDaLJ"
}

client = ibmiotf.device.Client(options)
client.connect()

myData={'bikeID':'1'}
x=0

while 1:
    if(x != GPIO.input(21)):
        x=GPIO.input(21)
        if(x == 1):
            print("Pedal "+time.strftime("%S"))
            client.publishEvent(event="pedal", msgFormat="json", data=myData)
    time.sleep(0.001)