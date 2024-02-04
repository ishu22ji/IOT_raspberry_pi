import RPi.GPIO as GP
GP.setwarnings(False)
import time
GP.setmode(GP.BCM)
##########################
GP.setup(17,GP.OUT)
GP.setup(22,GP.OUT)
GP.setup(27,GP.OUT)
GP.setup(24,GP.IN)
############################
pwm1 = GP.PWM(17,1000)
pwm2 = GP.PWM(22,1000)
pwm3 = GP.PWM(27,1000)
#############################
pwm1.start(10)
pwm2.start(10)
pwm3.start(10)

try:
    while True:
        pin1 = GP.input(24)
        
        if pin1 == 1:
            for i in range(100):
                print("the value of pwm x1 is=",i)
                pwm1.ChangeDutyCycle(i)
                pwm3.ChangeDutyCycle(i)
                pwm2.ChangeDutyCycle(i)
                time.sleep(0.1)
        else :
            pwm1.ChangeDutyCycle(10)
            pwm3.ChangeDutyCycle(10)
            pwm2.ChangeDutyCycle(10)
        

except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()
