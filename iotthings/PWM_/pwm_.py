import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(24, GPIO.IN)

pwm = GPIO.PWM(17, 1000)
pwm.start(0)

try:
    while True:
        pin1 = GPIO.input(24)
        if pin1 == 1:
            pwm.ChangeDutyCycle(10)
        elif pin1 == 0:
            pwm.ChangeDutyCycle(100)
        

except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()
