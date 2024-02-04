import RPi.GPIO as GP
import time

GP.setmode(GP.BCM)
GP.setwarnings(False)
GP.setup(24, GP.IN)
GP.setup(23, GP.IN)
l1 = [22, 27, 5]
l2 = [6, 13, 19]

GP.setup(l1, GP.OUT)
GP.setup(l2, GP.OUT)

try:
    while True:
        pin1 = GP.input(24)
        pin2 = GP.input(23)

        if pin1 == 0:
            for i in range(len(l1)):
                GP.output(l1[i], 0)
            print("yes 1")
        else:
            GP.output(l1, 1)
            print("nooo 1")

        if pin2 == 0:
            for i in range(len(l2)):
                GP.output(l2[i], 0)
            print("yes 2")
        else:
            GP.output(l2, 1)
            print("nooo 2")

        time.sleep(0.1)  # Add a small delay to avoid excessive printing

except KeyboardInterrupt:
    print("\nProgram stopped by the user.")

finally:
    GP.cleanup()
    print("GPIO cleanup completed. Exiting the program.")

