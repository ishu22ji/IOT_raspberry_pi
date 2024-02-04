import RPi.GPIO as GP
GP.setmode(GP.BCM)
GP.setup(17,GP.OUT)
GP.output(17,1)