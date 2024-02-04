import RPi.GPIO as GP
import time

GP.setmode(GP.BCM)
GP.setwarnings(False)
GP.setup(17, GP.OUT)
GP.setup(22, GP.OUT)
GP.setup(27, GP.OUT)
GP.setup(5, GP.OUT)
GP.setup(6, GP.OUT)
GP.setup(13, GP.OUT)
GP.setup(19, GP.OUT)

try:
    while True:
        input1 = input("Enter 'on' to turn on or 'off' to turn off, or 'stop' to end: ")
        if input1 == 'off':
            GP.output(17, 0)
            GP.output(22, 0)
            GP.output(19, 0)
            GP.output(5, 0)
            GP.output(6, 0)
            GP.output(13, 0)
            GP.output(27, 0)
        elif input1 == 'on':
            GP.output(17, 1)
            GP.output(22, 1)
            GP.output(19, 1)
            GP.output(5, 1)
            GP.output(6, 1)
            GP.output(13, 1)
            GP.output(27, 1)
        elif input1 == 'stop':
            break
        else:
            print("Invalid input. Please enter 'on', 'off', or 'stop'.")

except KeyboardInterrupt:
    print("\nProgram stopped by the user.")

finally:
    GP.cleanup()
    print("GPIO cleanup completed. Exiting the program.")
