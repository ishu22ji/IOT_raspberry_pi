import time
import requests
from ds18b20 import DS18B20
import dht11
import RPi.GPIO as GPIO
import time
import random
GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.IN)
GPIO.setwarnings(False)
req=dht11.DHT11(pin = 25)

def rohitprint():
    print("sada function")
    print("inside function")
    time.sleep(3)

def mypayload():
    pressure=random.randint(20,100)
    temp= DS18B20().get_temperature()
    print("Temp sent to cloud  %0.2f *C "%temp)
    time.sleep(3)
    a = req.read()
    tempx = a.temperature
    humx = a.humidity
 
    print("temperature = %0.2f c"%tempx)
    print("humidity = %0.2f percent"%humx)

    time.sleep(5)
    payload = {'dhttemp':tempx,'dhthum':humx,'mytemp':temp,'pressure1':pressure}
    return payload
while 1:
    rohitprint()
    

    try:
        r = requests.post('http://things.ubidots.com/api/v1.6/devices/myraspberry/?token=BBFF-6RNW5cSXxaGRdi0QHMChRR5Jir480u', data=mypayload())
        print('sending our temp to  ubidots')
      
    except:
        pass
        print("value nahin gayii check karo ji ")          
        time.sleep(3)

