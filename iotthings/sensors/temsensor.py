from ds18b20 import DS18B20
import time 
import RPi.GPIO as GP
import dht11
GP.setmode(GP.BCM)
GP.setwarnings(False)
GP.setup(25, GP.IN)
while 1:
    req = dht11.DHT11(pin=25)
    temp= DS18B20().get_temperature()
    print("Temperature %0.2f *C he bhai"%temp)
    if temp>30:
        print("Garam he")
    elif temp<23:
        print("Thanda he")
    else :
        print("Theek Thak He")
    time.sleep(1)
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