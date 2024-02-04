import RPi.GPIO as GP
import time
GP.setmode(GP.BCM)
GP.setwarnings(False)
pins=[17,22,27,5,6,13,19]

GP.setup(pins,GP.OUT)

while True:
	for i in range(len(pins)):
		GP.output(pins[i],1)
		time.sleep(0.2)
	for r in range(len(pins)):
		time.sleep(0.2)
		GP.output(pins[r],0)
		
except KeyboardInterrupt:
    print("\nProgram stopped by the user.")

finally:
    GP.cleanup()
    print("GPIO cleanup completed. Exiting the program.")





