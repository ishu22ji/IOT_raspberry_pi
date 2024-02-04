from Adafruit_IO import Client
from ds18b20 import DS18B20
import time
import RPi.GPIO as GPIO
import dht11

USERNAME = "ishinder"
KEY = "aio_HHzw59mfHqhrssff2fkfMZQqeCUV"
aio=Client(USERNAME,KEY)
################################
mytemp=aio.feeds("dstemp")
tempx=aio.feeds("temp")
humx=aio.feeds("humidity")
###################################
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(25, GPIO.IN)
dhread = dht11.DHT11(pin=25)
mytempx=20
myhumdx=20
while 1:
##############################################
    result = dhread.read()
    if result.is_valid():
        print("Reading Started")
        temp = result.temperature
        humd = result.humidity
        if temp>0:
            mytempx=temp
            myhumdx=humd
            print("Temperature = %0.2f°C" % mytempx)
            print("Humidity = %0.2f%%" % myhumdx)
            time.sleep(4)
        else:
            print("   -----reading not read dht11 ")
            time.sleep(2)      
##############################################              
    temp= DS18B20().get_temperature()
    print("Temp sent to cloud  %0.2f *C "%temp)
    time.sleep(7)
    aio.send(mytemp.key,temp)
    aio.send(tempx.key,mytempx)
    aio.send(humx.key,myhumdx)