import RPi.GPIO as GP
import time
import dht11

GP.setmode(GP.BCM)
GP.setwarnings(False)

# Set up the input and output pins
GP.setup(24, GP.IN)
GP.setup(23, GP.IN)
GP.setup(25, GP.IN)
l1 = [22, 27, 5]
l2 = [6, 13, 19]

# Set up each pin individually for output
for pin in l1:
    GP.setup(pin, GP.OUT)

for pin in l2:
    GP.setup(pin, GP.OUT)

try:
    while True:
        pin1 = GP.input(24)
        pin2 = GP.input(23)
        req = dht11.DHT11(pin=25)

        if pin1 == 0:
            for pin in l1:
                GP.output(pin, 0)
            print("yes 1")
        else:
            for pin in l1:
                GP.output(pin, 1)
            print("nooo 1")

        if pin2 == 0:
            for pin in l2:
                GP.output(pin, 0)
            print("yes 2")
        else:
            for pin in l2:
                GP.output(pin, 1)
            print("nooo 2")

        # Read temperature and humidity
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
                time.sleep(2)  # Add a small delay to avoid excessive printing

except KeyboardInterrupt:
    print("\nProgram stopped by the user.")

finally:
    GP.cleanup()
    print("GPIO cleanup completed. Exiting the program.")
