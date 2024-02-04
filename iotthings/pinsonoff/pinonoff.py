import RPi.GPIO as GP
import time
GP.setmode(GP.BCM)
GP.setwarnings(False)
GP.setup(17,GP.OUT)
GP.setup(22,GP.OUT)
GP.setup(27,GP.OUT)
GP.setup(5,GP.OUT)
GP.setup(6,GP.OUT)
GP.setup(13,GP.OUT)
GP.setup(19,GP.OUT)

while True:
    GP.output(17,0)
    GP.output(22,0)
    GP.output(27,0)
    GP.output(5,0)
    GP.output(6,0)
    GP.output(13,0)
    GP.output(19,0)



    time.sleep(1.5)

    GP.output(17,1)
    GP.output(22,1)
    GP.output(27,1)
    GP.output(5,1)
    GP.output(6,1)
    GP.output(13,1)
    GP.output(19,1)


    time.sleep(1)