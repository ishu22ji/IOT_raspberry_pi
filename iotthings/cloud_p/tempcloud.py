from Adafruit_IO import Client
import random
from ds18b20 import DS18B20
import time
import RPi.GPIO as GPIO
import dht11
USERNAME = "ishinder"
KEY = "aio_HHzw59mfHqhrssff2fkfMZQqeCUV"
aio=Client(USERNAME,KEY)
ran=aio.feeds("ishinder")

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(25, GPIO.IN)
req = dht11.DHT11(pin=25)
while 1:
    
    temp= DS18B20().get_temperature()
    aio.send(ran.key,temp)
    print("Temperature %0.2f *C he bhai"%temp)
	
    if temp>30:
        print("Garam he")
    elif temp<23:
        print("Thanda he")
    else :
        print("Theek Thak He")
    time.sleep(2)
    result = req.read()
    if result.is_valid():
        print("Reading Started")
        temp = result.temperature
        humd = result.humidity
        if temp>0:
            mytemp=temp
            myhumd=humd
            print("Temperature = %0.2f°C" % mytemp)
            print("Humidity = %0.2f%%" % myhumd)
            time.sleep(1)