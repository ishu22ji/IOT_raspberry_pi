import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)

while True:
    GPIO.output(17,0)
    time.seep(0.2)
    GPIO.output(17,1)
    time.seep(0.2)

    GPIO.output(17,0)
    GPIO.output(22,0)
    time.sleep(0.2)
    GPIO.output(22,1)
    GPIO.output(27,0)
    time.sleep(0.2)
    GPIO.output(27,1)
    GPIO.output(5,0)
    time.sleep(0.2)
    GPIO.output(5,1)
    GPIO.output(6,0)
    time.sleep(0.2)
    GPIO.output(6,1)
    GPIO.output(13,0)
    time.sleep(0.2)
    GPIO.output(13,1)
    GPIO.output(19,0)
    time.sleep(0.2)
    GPIO.output(19,1)