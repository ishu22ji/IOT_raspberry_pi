import dht11
import RPi.GPIO as GP
import time
GP.setmode(GP.BCM)
GP.setup(25,GP.IN)
GP.setwarnings(False)

while 1:
	req = dht11.DHT11(pin = 25)
	a = req.read()
	temp = a.temperature
	humd = a.humidity
	print("temperature = %0.2f c"%temp)
	print("humidity = %0.2f percent"%humd)
	time.sleep(5)