import time
from Adafruit_IO import Client
import RPi.GPIO as GPIO
from ds18b20 import DS18B20
import dht11

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(25, GPIO.IN)
req = dht11.DHT11(pin=25)

USERNAME = "ishinder"
KEY = "aio_HHzw59mfHqhrssff2fkfMZQqeCUV"
aio = Client(USERNAME, KEY)
myout = aio.feeds("outx")
isf = aio.feeds("ishinder")
GPIO.setup(27, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

while True:
    a = aio.receive(myout.key)
    if a.value == "ON":
        temp = DS18B20().get_temperature()
        aio.send(isf.key, temp)
        print("Temperature %0.2f *C he bhai" % temp)
        if temp > 30:
            print("Garam he")
        elif temp < 23:
            print("Thanda he")
        else:
            print("Theek Thak He")
        time.sleep(2)
        GPIO.output(27, 1)
    else:
        GPIO.output(27, 0)
        print("LED 1 is OFF")
