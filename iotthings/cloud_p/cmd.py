import time
from Adafruit_IO import Client
import RPi.GPIO as GPIO
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)  # Setup GPIO pin 27 as an output pin

USERNAME = "ishinder"
KEY = "aio_HHzw59mfHqhrssff2fkfMZQqeCUV"
aio = Client(USERNAME, KEY)
myout = aio.feeds("outx")

while True:
    a = aio.receive(myout.key)
    os.system(a.value)  # You may need to add a specific command here if a.value is a valid command
    print(a.value)
    if a.value == "ON":  # Removed unnecessary parentheses and extra whitespace
        GPIO.output(27, 1)
        print("LED 1 is ON")
    elif a.value == "OFF":  # Removed unnecessary parentheses and extra whitespace
        GPIO.output(27, 0)
        print("LED 1 is OFF")
    time.sleep(5)
